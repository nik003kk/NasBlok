import test, { beforeEach, afterEach } from 'node:test'
import assert from 'node:assert/strict'
import { api, getToken, setToken } from '../src/api.js'

const savedFetch = globalThis.fetch
const savedLocalStorage = globalThis.localStorage
let storage

beforeEach(() => {
  storage = new Map()
  globalThis.localStorage = {
    getItem: key => storage.get(key) ?? null,
    setItem: (key, value) => storage.set(key, value),
    removeItem: key => storage.delete(key),
  }
})

afterEach(() => {
  globalThis.fetch = savedFetch
  globalThis.localStorage = savedLocalStorage
})

test('token can be saved and read', () => {
  setToken('abc123')
  assert.equal(getToken(), 'abc123')
})

test('token can be removed', () => {
  setToken('abc123')
  setToken(null)
  assert.equal(getToken(), null)
})

test('GET request uses /api prefix', async () => {
  globalThis.fetch = async (url, opts) => {
    assert.equal(url, '/api/auth/me')
    assert.equal(opts.method, 'GET')
    return { ok: true, status: 200, json: async () => ({ id: 1 }) }
  }
  assert.deepEqual(await api('/auth/me'), { id: 1 })
})

test('authorized request includes bearer token', async () => {
  setToken('test-token')
  globalThis.fetch = async (_url, opts) => {
    assert.equal(opts.headers.Authorization, 'Bearer test-token')
    return { ok: true, status: 200, json: async () => ({ ok: true }) }
  }
  await api('/auth/me')
})

test('POST sends JSON body', async () => {
  globalThis.fetch = async (_url, opts) => {
    assert.equal(opts.method, 'POST')
    assert.equal(opts.headers['Content-Type'], 'application/json')
    assert.equal(opts.body, JSON.stringify({ name: 'Blok A' }))
    return { ok: true, status: 201, json: async () => ({ id: 2 }) }
  }
  await api('/buildings', { method: 'POST', body: { name: 'Blok A' } })
})

test('204 response returns null', async () => {
  globalThis.fetch = async () => ({ ok: true, status: 204 })
  assert.equal(await api('/buildings/1/units/2', { method: 'DELETE' }), null)
})

test('API returns descriptive server error', async () => {
  globalThis.fetch = async () => ({ ok: false, status: 403, json: async () => ({ detail: 'Ni dostopa.' }) })
  await assert.rejects(() => api('/buildings/1'), err => err.status === 403 && err.message === 'Ni dostopa.')
})

test('validation error array gets safe generic message', async () => {
  globalThis.fetch = async () => ({ ok: false, status: 422, json: async () => ({ detail: [{ msg: 'invalid' }] }) })
  await assert.rejects(() => api('/auth/register'), /Preverite vnesene podatke\./)
})
