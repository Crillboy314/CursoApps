// ════════════════════════════════════════════════════════
// LIBRO DE VISITAS — el lab completo de la Sesión 5
// Requiere: uvicorn main:app --reload  corriendo
// ════════════════════════════════════════════════════════

const API = 'http://127.0.0.1:8000';

const inputNombre  = document.getElementById('input-nombre');
const inputMensaje = document.getElementById('input-mensaje');
const boton        = document.getElementById('btn-enviar');
const lista        = document.getElementById('lista-visitas');

// ── EL PATRÓN DE 3 PASOS: pedir → recorrer → pintar ──────
function recargarLista() {
  fetch(`${API}/visitas`)                    // 1. pedir
    .then(r => r.json())
    .then(datos => {
      let html = '';
      datos.visitas.forEach(v => {           // 2. recorrer
        html += `<div class="item">
                   <b>${v.nombre}</b>: ${v.mensaje}
                 </div>`;
      });
      lista.innerHTML = html;                // 3. pintar
    });
}

// ── EL POST: enviar datos a tu API ───────────────────────
boton.addEventListener('click', () => {

  // Validación mínima en el front
  if (!inputNombre.value || !inputMensaje.value) {
    alert('Llena los dos campos 🙃');
    return;
  }

  fetch(`${API}/visitas`, {
    method: 'POST',                          // 1. el método
    headers: { 'Content-Type': 'application/json' },  // 2. avisar que es JSON
    body: JSON.stringify({                   // 3. los datos
      nombre:  inputNombre.value,
      mensaje: inputMensaje.value,
    })
  })
    .then(r => r.json())
    .then(() => {
      // Limpiar inputs y REPINTAR la lista
      inputNombre.value  = '';
      inputMensaje.value = '';
      recargarLista();   // ← la clave: el dato nuevo aparece
    })
    .catch(err => alert('❌ ¿Está corriendo uvicorn? ' + err));
});

// Al abrir la página, cargar lo que ya exista
recargarLista();

// ════════════════════════════════════════════════════════
// 💡 PARA LA CLASE:
// 1. Envía una visita y mira la pestaña Network (F12):
//    verás el POST y luego el GET. Dos peticiones.
// 2. Reinicia uvicorn → la lista se vacía. ¿Por qué?
//    Porque VISITAS vive en memoria. Eso se arregla con
//    una base de datos (lo veremos más adelante).
// 3. Esto que hicimos a mano (repintar tras cada cambio)
//    es EXACTAMENTE lo que React automatiza con useState.
// ════════════════════════════════════════════════════════
