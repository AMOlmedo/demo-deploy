# Restaurar un Repositorio Git y Hacer Push a GitHub desde Cero

Este documento sirve como referencia rápida para los pasos necesarios luego de eliminar el directorio `.git` y querer volver a subir tu proyecto limpio a un repositorio en GitHub.

## 1. Eliminar el seguimiento anterior (opcional)

Si el repositorio estaba en mal estado, se puede borrar el seguimiento anterior:

```bash
rm -rf .git
```

## 2. Inicializar nuevamente Git

```bash
git init
```

## 3. Agregar todos los archivos al staging area

```bash
git add .
```

## 4. Hacer el primer commit

```bash
git commit -m "Primer commit del proyecto limpio"
```

## 5. Crear la rama principal (`main`)

```bash
git branch -M main
```

## 6. Agregar el repositorio remoto

```bash
git remote add origin git@github.com:TU_USUARIO/TU_REPO.git
```

Reemplazá `TU_USUARIO` y `TU_REPO` con tu nombre de usuario y el nombre del repositorio real.

> Podés verificar que esté bien agregado con:

```bash
git remote -v
```

## 7. Hacer push al repositorio en GitHub

```bash
git push -f origin main
```

Usamos el parámetro `-f` (force) ya que es un push inicial y puede sobrescribir el historial previo.

---

### Extras útiles

* Si GitHub te da errores de autenticación por `publickey`, asegurate de tener configurada tu **clave SSH** correctamente y que esté añadida a tu cuenta de GitHub.

* Si no ves los archivos en GitHub tras el push, asegurate de estar empujando a la rama correcta (`main`) y al repositorio correcto (revisá la URL remota con `git remote -v`).

---

¡Listo! Con esto deberías poder reconstruir tu proyecto en GitHub desde cero sin problemas. ✅
