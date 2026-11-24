import test from 'node:test'
import assert from 'node:assert/strict'
import { ROLE_LABELS, VOTING_ROLES, ANNOUNCEMENT_ROLES } from '../src/auth/roles.js'

test('owner can vote', () => assert.ok(VOTING_ROLES.includes('OWNER')))
test('tenant cannot vote', () => assert.ok(!VOTING_ROLES.includes('TENANT')))
test('contractor cannot vote', () => assert.ok(!VOTING_ROLES.includes('CONTRACTOR')))
test('tenant can read announcements', () => assert.ok(ANNOUNCEMENT_ROLES.includes('TENANT')))
test('contractor cannot read announcements', () => assert.ok(!ANNOUNCEMENT_ROLES.includes('CONTRACTOR')))
test('manager has role label', () => assert.equal(ROLE_LABELS.MANAGER, 'upravnik'))
