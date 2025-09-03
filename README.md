# team-notes

Mini app de consola para gestionar notas de texto.

## 🚀 Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/team-notes.git
   cd team-notes# team-notes

Flujo de trabajo en equipo

- Cada issue → una rama `feature/<id>-<desc>` → PR a `develop` → 1 aprobación → "Squash and merge".
- Conflicto obligatorio: dos issues deben editar la misma sección del README (“Uso”) para simular un conflicto y resolverlo.
- Prohibido hacer push directo a `main` (está protegida).
- Entrega final: PR `develop` → `main`, crear tag `v1.0.0` y Release con notas desde CHANGELOG.md.

Checklist de verificación rápida

- [✅ ] Colaboradores invitados al repo
- [✅ ] Rama `develop` creada y puesta como default
- [✅ ] Rama `main` protegida (PR obligatoria, 1 review, bloquear force push y borrado)
- [✅ ] Templates en `.github/` cargados (PR template)
- [✅ ] Milestone `v1.0.0` creado
- [✅ ] 6 issues creados y asignados

Flujo:
1) Tomá un issue asignado y creá la rama: `feature/<id>-<desc>`
2) Hacé commits chicos con la convención (`feat`, `fix`, `docs`, `test`, etc.)
3) Subí la rama y abrí PR hacia `develop`. Título: "feat: <resumen>"
4) Pedí 1 review. Resolvé comentarios.
5) Hacé "Squash and merge".
6) Al final: PR de `develop` a `main`, tag `v1.0.0` y Release.