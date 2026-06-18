// ════════════════════════════════════════════════════════
// PASO 2: fetch() a una API externa
// La MISMA URL que usaron en Thunder Client en la Sesión 2
// ════════════════════════════════════════════════════════

// 1. La URL que ya conocen de Thunder Client
const URL = 'https://jsonplaceholder.typicode.com/posts/1';

// 2. Seleccionar los elementos (Bloque 1 de JS)
const boton = document.getElementById('btn-traer');
const caja  = document.getElementById('resultado');

// 3. Escuchar el click (Bloque 2 de JS)
boton.addEventListener('click', () => {

  caja.textContent = 'Cargando... ⏳';

  // 4. fetch() — Bloque 3. Es EXACTAMENTE lo que hacía
  //    Thunder Client al presionar "Send":
  fetch(URL)
    .then(respuesta => respuesta.json())  // convertir a JSON
    .then(datos => {
      // "datos" es el mismo JSON que veían en Thunder Client
      console.log(datos);  // 👀 míralo en la consola (F12)

      // Mostrar el título del post en pantalla
      caja.innerHTML = `
        <strong>Título:</strong> ${datos.title}<br><br>
        <strong>Cuerpo:</strong> ${datos.body}
      `;
    })
    .catch(error => {
      // Si algo falla (sin internet, URL mala, etc.)
      caja.textContent = '❌ Error: ' + error;
    });

});