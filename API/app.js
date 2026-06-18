// ════════════════════════════════════════════════════════
// PASO 3: Tu HTML consume TU PROPIA API
//
// ⚠️ REQUISITO: la API debe estar corriendo.
//    En una terminal aparte:  uvicorn main:app --reload
//
// 💡 LA ÚNICA DIFERENCIA con el Paso 2:
//    la URL ya no es jsonplaceholder...
//    ahora es TU servidor: http://127.0.0.1:8000
// ════════════════════════════════════════════════════════

const API = 'http://127.0.0.1:8000';

const caja = document.getElementById('resultado');

// ── Botón 1: /sobre-mi ───────────────────────────────────
document.getElementById('btn-sobre-mi')
  .addEventListener('click', () => {
    fetch(`${API}/sobre-mi`)
      .then(r => r.json())
      .then(datos => {
        caja.innerHTML = `
          <strong>${datos.nombre}</strong><br>
          📍 ${datos.ciudad}<br>
          💼 ${datos.profesion}
        `;
      })
      .catch(err => caja.textContent = '❌ ¿Está corriendo uvicorn? ' + err);
  });

// ── Botón 2: /frase-aleatoria ────────────────────────────
document.getElementById('btn-frase')
  .addEventListener('click', () => {
    fetch(`${API}/frase-aleatoria`)
      .then(r => r.json())
      .then(datos => {
        caja.innerHTML = `<em>"${datos.frase}"</em>`;
      })
      .catch(err => caja.textContent = '❌ ¿Está corriendo uvicorn? ' + err);
  });

// ── Botón 3: /peliculas (recorrer una lista) ─────────────
document.getElementById('btn-peliculas')
  .addEventListener('click', () => {
    fetch(`${API}/peliculas`)
      .then(r => r.json())
      .then(datos => {
        // datos.peliculas es una LISTA → la recorremos
        let html = '<strong>Mis películas:</strong><br>';
        datos.peliculas.forEach(peli => {
          html += `🎬 ${peli.titulo} (${peli.anio})<br>`;
        });
        caja.innerHTML = html;
      })
      .catch(err => caja.textContent = '❌ ¿Está corriendo uvicorn? ' + err);
  });
