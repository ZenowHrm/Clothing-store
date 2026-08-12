// assets/editor.js

window.canvasEditor = null;

// ==========================================
// SISTEMA DE HISTORIAL (DESHACER / REHACER)
// ==========================================
window.historial = [];
window.pasoHistorial = -1;
window.bloquearHistorial = false;

window.guardarEstado = function() {
    if (!window.canvasEditor || window.bloquearHistorial) return;
    
    // Si estábamos en medio del historial y hacemos una nueva acción, borramos el futuro
    if (window.pasoHistorial < window.historial.length - 1) {
        window.historial = window.historial.slice(0, window.pasoHistorial + 1);
    }
    
    window.historial.push(JSON.stringify(window.canvasEditor.toJSON()));
    window.pasoHistorial++;
};

window.deshacer = function() {
    if (window.pasoHistorial <= 0) return;
    window.pasoHistorial--;
    window.restaurarEstado(window.historial[window.pasoHistorial]);
};

window.rehacer = function() {
    if (window.pasoHistorial >= window.historial.length - 1) return;
    window.pasoHistorial++;
    window.restaurarEstado(window.historial[window.pasoHistorial]);
};

window.restaurarEstado = function(estadoJson) {
    if (!window.canvasEditor || !estadoJson) return;
    window.bloquearHistorial = true;
    window.canvasEditor.loadFromJSON(estadoJson, () => {
        window.canvasEditor.renderAll();
        window.bloquearHistorial = false;
    });
};

// ==========================================
// 1. INICIALIZAR EL LIENZO
// ==========================================
window.initCanvas = function() {
    if (window.canvasEditor) return;

    if (typeof fabric === 'undefined') {
        console.error("Fabric.js aún no se ha cargado.");
        return;
    }

    const el = document.getElementById("lienzo-canva");
    const w = el ? el.clientWidth : 800;
    const h = el ? el.clientHeight : 600;

    window.canvasEditor = new fabric.Canvas("lienzo-canva", {
        backgroundColor: "#ffffff",
        isDrawingMode: false
    });

    window.canvasEditor.setWidth(w);
    window.canvasEditor.setHeight(h);
    window.canvasEditor.renderAll();

    // Eventos para registrar en el historial
    window.canvasEditor.on('object:added', window.guardarEstado);
    window.canvasEditor.on('object:modified', window.guardarEstado);
    window.canvasEditor.on('object:removed', window.guardarEstado);

    // Guardar estado inicial vacío
    window.guardarEstado();
};

// ==========================================
// 2. COLOR DE FONDO DEL LIENZO
// ==========================================
window.cambiarColorLienzo = function(color = "#ffffff") {
    if (!window.canvasEditor) return;
    window.canvasEditor.setBackgroundColor(color, window.canvasEditor.renderAll.bind(window.canvasEditor));
    window.guardarEstado();
};

// ==========================================
// 3. MODO DE DIBUJO LIBRE (PINCEL)
// ==========================================
window.toggleModoDibujo = function(activar = null) {
    if (!window.canvasEditor) return;
    window.canvasEditor.isDrawingMode = activar !== null ? activar : !window.canvasEditor.isDrawingMode;
};

window.cambiarColorPincel = function(color = "#000000") {
    if (!window.canvasEditor) return;
    window.canvasEditor.freeDrawingBrush.color = color;
};

window.cambiarTamanoPincel = function(tamano = 5) {
    if (!window.canvasEditor) return;
    window.canvasEditor.freeDrawingBrush.width = parseInt(tamano, 10) || 5;
};

// ==========================================
// 4. TEXTO, COLORES Y FUENTES
// ==========================================
window.fuentesDisponibles = [
    'Arial', 'Courier New', 'Georgia', 'Times New Roman', 
    'Verdana', 'Impact', 'Comic Sans MS', 'Trebuchet MS'
];

window.agregarTexto = function(textoInicial = "Doble clic para editar", opciones = {}) {
    if (!window.canvasEditor) return;

    const texto = new fabric.IText(textoInicial, {
        left: 150,
        top: 150,
        fontFamily: opciones.fuente || 'Arial',
        fill: opciones.color || '#333333',
        fontSize: opciones.tamano || 28
    });

    window.canvasEditor.add(texto);
    window.canvasEditor.setActiveObject(texto);
};

window.cambiarColorSeleccionado = function(color = "#000000") {
    if (!window.canvasEditor) return;
    const obj = window.canvasEditor.getActiveObject();
    if (!obj) return;

    if (obj.type === 'i-text' || obj.type === 'text') {
        obj.set('fill', color);
    } else if (obj.fill && obj.fill !== 'transparent') {
        obj.set('fill', color);
    } else if (obj.stroke) {
        obj.set('stroke', color);
    }
    window.canvasEditor.renderAll();
    window.guardarEstado();
};

window.cambiarFuenteTexto = function(fuente = "Arial") {
    if (!window.canvasEditor) return;
    const obj = window.canvasEditor.getActiveObject();
    if (obj && (obj.type === 'i-text' || obj.type === 'text')) {
        obj.set('fontFamily', fuente);
        window.canvasEditor.renderAll();
        window.guardarEstado();
    }
};

// ==========================================
// 5. AGREGAR IMÁGENES (DESDE URL O ARCHIVO)
// ==========================================
window.agregarImagenDesdeURL = function(url) {
    if (!window.canvasEditor || !url) return;
    fabric.Image.fromURL(url, function(img) {
        img.set({
            left: 100,
            top: 100,
            scaleX: 0.5,
            scaleY: 0.5
        });
        window.canvasEditor.add(img);
        window.canvasEditor.setActiveObject(img);
    }, { crossOrigin: 'anonymous' });
};

// Puedes pasar directamente un Input Event de tipo <input type="file" />
window.agregarImagenDesdeArchivo = function(file) {
    if (!file || !window.canvasEditor) return; 

    const reader = new FileReader();
    reader.onload = function(e) {
        window.agregarImagenDesdeURL(e.target.result); 
    };
    reader.readAsDataURL(file);
};

// ==========================================
// 6. FIGURAS GEOMÉTRICAS (HUECAS O RELLENAS)
// ==========================================
window.agregarFigura = function(tipo = 'rectangulo', color = '#4A90E2', hueco = true) {
    if (!window.canvasEditor) return;

    const configEstilo = hueco 
        ? { fill: 'transparent', stroke: color, strokeWidth: 3 }
        : { fill: color, stroke: '', strokeWidth: 0 };

    let figura = null;

    switch (tipo.toLowerCase()) {
        case 'rectangulo':
            figura = new fabric.Rect({
                left: 100,
                top: 100,
                width: 120,
                height: 120,
                ...configEstilo
            });
            break;
        case 'circulo':
            figura = new fabric.Circle({
                left: 100,
                top: 100,
                radius: 60,
                ...configEstilo
            });
            break;
        case 'triangulo':
            figura = new fabric.Triangle({
                left: 100,
                top: 100,
                width: 120,
                height: 120,
                ...configEstilo
            });
            break;
        case 'linea':
            figura = new fabric.Line([50, 50, 200, 50], {
                left: 100,
                top: 100,
                stroke: color,
                strokeWidth: 4
            });
            break;
    }

    if (figura) {
        window.canvasEditor.add(figura);
        window.canvasEditor.setActiveObject(figura);
    }
};

// ==========================================
// 7. BORRAR SELECCIONADO
// ==========================================
window.borrarSeleccionado = function() {
    if (!window.canvasEditor) return;

    const activos = window.canvasEditor.getActiveObjects();
    if (!activos.length) return;

    activos.forEach(obj => window.canvasEditor.remove(obj));
    window.canvasEditor.discardActiveObject().renderAll();
    window.guardarEstado();
};

// ==========================================
// 8. EXPORTAR A PNG, JPG Y PDF
// ==========================================
window.descargarArchivo = function(dataURL, nombreArchivo) {
    const a = document.createElement('a');
    a.href = dataURL;
    a.download = nombreArchivo;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
};

window.exportarPNG = function(nombre = "diseno.png") {
    if (!window.canvasEditor) return;
    const dataURL = window.canvasEditor.toDataURL({
        format: 'png',
        quality: 1
    });
    window.descargarArchivo(dataURL, nombre);
};

window.exportarJPG = function(nombre = "diseno.jpg") {
    if (!window.canvasEditor) return;
    // JPG no soporta transparencias, un fondo transparente en JPG se ve negro.
    // Garantizamos fondo blanco temporal si estaba transparente:
    const colorAnterior = window.canvasEditor.backgroundColor;
    if (!colorAnterior || colorAnterior === 'transparent') {
        window.canvasEditor.setBackgroundColor('#ffffff', null);
    }
    window.canvasEditor.renderAll();

    const dataURL = window.canvasEditor.toDataURL({
        format: 'jpeg',
        quality: 0.95
    });
    window.descargarArchivo(dataURL, nombre);

    // Revertir fondo si era necesario
    if (!colorAnterior || colorAnterior === 'transparent') {
        window.canvasEditor.setBackgroundColor(colorAnterior, window.canvasEditor.renderAll.bind(window.canvasEditor));
    }
};

// Nota: Para exportar a PDF necesitas incluir en tu HTML la librería jsPDF:
// <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
window.exportarPDF = function(nombre = "diseno.pdf") {
    if (!window.canvasEditor) return;

    if (!window.jspdf || !window.jspdf.jsPDF) {
        alert("Para exportar a PDF asegúrate de haber cargado la librería jsPDF en tu HTML.");
        return;
    }

    const { jsPDF } = window.jspdf;
    const ancho = window.canvasEditor.getWidth();
    const alto = window.canvasEditor.getHeight();
    const orientacion = ancho > alto ? 'l' : 'p';

    const doc = new jsPDF({
        orientation: orientacion,
        unit: 'px',
        format: [ancho, alto]
    });

    const dataURL = window.canvasEditor.toDataURL({
        format: 'png',
        quality: 1
    });

    doc.addImage(dataURL, 'PNG', 0, 0, ancho, alto);
    doc.save(nombre);
};

// ==========================================
// 9. ZOOM Y PAN
// ==========================================

function setupZoomPan() {
    const container = document.getElementById('canvas-container');
    const wrapper = document.getElementById('canvas-wrapper');
    
    if (!container || !wrapper) return;

    // --- LA SOLUCIÓN MÁGICA AQUÍ ---
    wrapper.style.setProperty("transform-origin", "0px 0px", "important");

    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let panning = false;
    let start = { x: 0, y: 0 };

    function centerCanvas() {
        const containerRect = container.getBoundingClientRect();
        
        // Leemos el tamaño real del lienzo dinámicamente en lugar de usar 500
        const wrapperWidth = wrapper.offsetWidth;
        const wrapperHeight = wrapper.offsetHeight;

        pointX = (containerRect.width - wrapperWidth) / 2;
        pointY = (containerRect.height - wrapperHeight) / 2;
        
        setTransform();
    }

    function setTransform() {
        wrapper.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
    }

    setTimeout(centerCanvas, 100); 

    // --- 1. ZOOM CORREGIDO HACIA EL PUNTERO ---
    container.addEventListener('wheel', (e) => {
        e.preventDefault();
        
        const rect = container.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        const isZoomingIn = e.deltaY < 0; 
        const delta = isZoomingIn ? 1.1 : 0.9; 
        
        let newScale = scale * delta;
        newScale = Math.min(Math.max(0.2, newScale), 5); // Límites de zoom
        
        // --- TU MATEMÁTICA ORIGINAL INTACTA ---
        const unscaledX = (mouseX - pointX) / scale;
        const unscaledY = (mouseY - pointY) / scale;

        const zoomOffsetX = mouseX - (unscaledX * newScale);
        const zoomOffsetY = mouseY - (unscaledY * newScale);

        pointX -= zoomOffsetX - pointX;
        pointY -= zoomOffsetY - pointY;

        scale = newScale;

        setTransform();
    }, { passive: false });


    // --- 2. MOVER EL LIENZO ---
    container.addEventListener('mousedown', (e) => {
        if (e.button === 1 || e.button === 2) { 
            e.preventDefault();
            panning = true;
            start = { x: e.clientX - pointX, y: e.clientY - pointY };
            container.style.cursor = 'grabbing';
        }
    });

    container.addEventListener('mousemove', (e) => {
        if (!panning) return;
        e.preventDefault();
        pointX = e.clientX - start.x;
        pointY = e.clientY - start.y;
        setTransform();
    });

    window.addEventListener('mouseup', () => {
        panning = false;
        container.style.cursor = 'default';
    });

    container.addEventListener('contextmenu', e => e.preventDefault());
}