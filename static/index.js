        const carritoBtn = document.getElementById('carritoBtn');
        const carritoSlider = document.getElementById('carritoSlider');
        const cerrarCarrito = document.getElementById('cerrarCarrito');

        carritoBtn.addEventListener('click', function (e) {
            e.preventDefault();
            carritoSlider.style.right = '0';
        });

        cerrarCarrito.addEventListener('click', function () {
            carritoSlider.style.right = '-350px';
        });