# NašBlok
[![NasBlok CI/CD](https://github.com/nik003kk/NasBlok/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/nik003kk/NasBlok/actions/workflows/ci-cd.yml)

NašBlok je spletna aplikacija za upravljanje večstanovanjske stavbe. Stanovalci v njej prijavljajo okvare in spremljajo njihovo reševanje, lastniki glasujejo o sklepih stavbe, upravnik pa objavlja obvestila in okvare dodeljuje serviserjem. Tako komunikacija v bloku ne poteka več na papirju, po telefonu in v WhatsApp skupinah, ampak na enem mestu.

Uporabniške vloge: etažni lastnik, najemnik, predstavnik lastnikov, upravnik in serviser.

## Tehnologije

- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** Python, FastAPI
- **Podatkovna baza:** PostgreSQL, SQLAlchemy, Alembic
- **Avtentikacija:** JWT, bcrypt
- **E-pošta:** fastapi-mail, Mailpit (razvoj), Brevo
- **Lokalni razvoj:** Docker, Git in GitHub

## Struktura projekta

```
├── frontend/   React aplikacija
├── backend/    FastAPI strežnik
└── docs/       dokumentacija projektas
```

## Dokumentacija

- [Zasnova rešitve](docs/01-zasnova-resitve.md)
- [Funkcionalnosti in obseg](docs/02-funkcionalnosti-in-obseg.md)
- [Podatkovni model](docs/03-podatkovni-model.md)
- [Arhitektura in tehnološki sklad](docs/04-arhitektura-in-tehnoloski-sklad.md)
- [Uporabniške zgodbe](docs/05-uporabniske-zgodbe.md)
- [Wireframi](docs/06-wireframes.md)
- [Arhitekturne odločitve (ADR)](docs/adr/)



## Produkcijska namestitev

Aplikacija NašBlok je javno dostopna na naslednjih naslovih:

- **Frontend (React):** https://nasblok-frontend.pages.dev
- **Backend (FastAPI):** https://nasblokbackend-production.up.railway.app
- **API dokumentacija:** https://nasblokbackend-production.up.railway.app/docs

Frontend je nameščen na Cloudflare Pages, backend in podatkovna baza PostgreSQL pa na platformi Railway.

Frontend se z backendom povezuje prek okoljske spremenljivke `VITE_API_URL`. Backend za povezavo s podatkovno bazo uporablja `DATABASE_URL`.

## CI/CD – GitHub Actions

Projekt uporablja avtomatiziran CI/CD cevovod, definiran v datoteki `.github/workflows/ci-cd.yml`.

Cevovod vsebuje štiri faze:

1. **Lint** – preverjanje kakovosti kode z ESLint za frontend in Ruff za backend.
2. **Build** – gradnja React aplikacije, preverjanje Python kode, priprava backend paketa in gradnja Docker slike. Rezultati se shranijo kot GitHub Actions artefakti.
3. **Test** – izvajanje avtomatiziranih frontend in backend testov ter priprava poročil o pokritosti kode.
4. **Deploy** – po uspešnih fazah Lint, Build in Test se ob pushu v vejo `main` izvedeta objava frontenda na Cloudflare Pages in namestitev backenda na Railway. Uporabijo se artefakti iz faze Build, brez ponovne gradnje.

### Sprožilci cevovoda

- **Pull Request v `main` ali `development`:** izvedejo se Lint, Build in Test.
- **Push v `main`:** po uspešnih preverjanjih se izvede tudi Deploy.

Veja `main` je zaščitena z obveznimi preverjanji Lint, Build in Test. Če katero preverjanje ni uspešno, združitev Pull Requesta ni dovoljena.

Občutljivi podatki za produkcijsko objavo so shranjeni v GitHub Actions Secrets, javne konfiguracijske vrednosti pa v GitHub Actions Variables.
