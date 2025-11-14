# 🏢 Technical Handbook

---

# 📌 **1. Welcome & Vision**

## **Purpose of This Handbook**

- Define how we build software.
- Ensure consistency, quality, and alignment across all teams.
- Serve as onboarding documentation for new engineers.

## **Engineering Principles**

- We build using clean architecture across all stacks.
- We prioritize maintainability over speed.
- We automate tests, deployments, and repetitive workflows.
- We invest in readability and clarity.
- Security is everyone's responsibility.

---

# 📌 **2. Tech Stack Overview**

## **Frontend**

- **Next.js** (App Router)
- **TanStack Query** for async state
- **Zustand or Redux Toolkit** for client state
- **TailwindCSS** for styling
- **shadcn/ui** for components
- **Clean Architecture** applied with:
    - presentation layer
    - domain layer
    - application layer (services, hooks)
    - infrastructure layer (API clients)

## **Backend**

- **NestJs + TypeScript**
- **Clean Architecture**
- **TypeORM**
- **PostgreSQL**
- **MongoDB** (when document DB needed)
- **Docker & Docker Compose**
- **REST API architecture**

## **Tooling**

- GitHub / GitHub Actions
- Docker
- Postman / Insomnia
- Vercel / Railway / DigitalOcean

---

# 📌 **3. Project Structure Guidelines**

## **Frontend (Next.js)**

### Folder Structure

Check the template repository for clean architecture on frontend:

[https://github.com/kaeyros-analytics-org/nextjs-starter-template](https://github.com/kaeyros-analytics-org/nextjs-starter-template)

### Rules

- Keep components small and pure.
- No business logic in UI components.
- All server communication through application services.
- React Server Components for data-fetching when possible.

### State Management

- Use **TanStack Query** for data-fetching state.
- Use **Zustand or Redux Toolkit** for UI/ephemeral/local state.

---

## **Backend (NestJs + Clean Architecture)**

### Folder Structure

Check the template repository for clean architecture on Backend:

[https://github.com/kaeyros-analytics-org/nestjs-starter](https://github.com/kaeyros-analytics-org/nestjs-starter)

### Rules

- **Controllers** must not contain business logic.
- **Use cases** contain business rules.
- **Repositories** implement domain contracts.
- **TypeORM models** stay in the infrastructure layer.
- **DTOs** validate all incoming/outgoing data.

---

# 📌 **4. Coding Standards**

## TypeScript Rules

- Always enable `strict: true`.

## Naming Conventions on frontend

- Files: `PascalCase`
- React components: `PascalCase`
- Variables: `camelCase`
- Classes: `PascalCase`
- Folders: `snake-case`

## Naming Conventions on backend

- Files: `snake-case`
- Variables: `camelCase`
- Classes: `PascalCase`
- Folders: `snake-case`

## Error Handling

- Backend uses standardized Error classes.
- Frontend uses `useErrorBoundary` when needed.
- Never swallow errors.

---

# 📌 **5. Git Workflow**

## Branching Model

- `main` — production
- `develop` — staging
- `feature/<name>` — features
- `bugfix/<name>` — fixes
- `hotfix/<name>` — urgent production fixes

## Commit Style (Conventional Commits)

- `feat: add user login`
- `fix: correct email validation`
- `refactor: simplify auth service`
- `chore: update dependencies`
- `docs: update README`

## Pull Request Rules

- Small PRs only
- Must include description
- At least 1 reviewer required
- CI must pass before merge

---

# 📌 **6. Architecture Standards**

## Clean Architecture Guidelines

- **Domain** contains entities + domain logic only.
- **Application** holds use cases + orchestrates domain.
- **Infrastructure** contains external services (DB, APIs).
- **Presentation** handles user interaction.

## Database Policy

- PostgreSQL for relational data.
- MongoDB for document/event data.
- TypeORM as unified data access layer.

## Caching

- Avoid caching unless necessary.
- Use Redis (optional future expansion).

---

# 📌 **7. Security Guidelines**

## API Security

- JWT Access/Refresh tokens
- Rate limiting required on all auth routes
- Validate all input using DTOs

## Data Protection

- Never commit `.env` files
- Use Hashing for passwords (bcrypt)
- Use HTTPS everywhere

---

# 📌 **8. Testing Standards**

## Types of Tests

- Unit tests (Jest)
- Integration tests
- E2E tests (Playwright or similar)

## Expectations

- Critical use cases must have test coverage
- Backend services tested against test containers

---

# 📌 **9. DevOps & CI/CD**

## Environments

- Local
- Staging
- Production

## CI/CD Rules

- Lint → Test → Build → Deploy
- PR must pass all steps

## Docker Standards

- Every backend project includes a `Dockerfile`
- Local setup uses `docker-compose` to spin up DB services

Example `docker-compose` includes:

- postgres
- mongo
- pgadmin (optional)
- api service

---

# 📌 **10. Documentation & Onboarding**

## README Template

- Overview
- Folder structure
- How to run project locally
- API documentation
- Environment variable list

## New Developer Onboarding

- Install required tools
- Clone repos
- Run `docker-compose up`
- Request access to secrets and platforms

---

# 📌 **11. Communication & Team Processes**

- Daily standups
- Sprint planning every 2 weeks
- Retros every sprint
- Use Teams for async communication
- Use GitHub issues for task tracking

---

# 📌 **12. Quality & Performance**

## UI/UX Quality

- Use shadcn components before writing custom ones
- Ensure responsiveness
- Follow design system

## Performance

- Use RSC for heavy data fetching
- Use TanStack Query caching wisely
- Avoid over-fetching on frontend
- Use DB indexes on backend

---

# 📌 **13. Appendix**

- Glossary
- ADR (Architecture Decision Record) templates
- Coding examples
- Boilerplate repositories

---

# ✔️ End of Template

You can now fill this section-by-section directly in Notion. Add toggles, subpages, or callouts to make the structure more interactive.