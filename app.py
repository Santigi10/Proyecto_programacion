from flask import Flask, render_template, request, redirect

app = Flask(__name__)

carrito_de_compras = {}

@app.route("/", methods=["GET", "POST"])

def index():
    total = sum(info['cantidad'] * info['precio'] for info in carrito_de_compras.values())
    print("Total del carrito:", total)
    return render_template("index.html", carrito = carrito_de_compras, total_pro=total)






@app.route("/carrito", methods=["GET", "POST"])
def carrito():
    if request.method == "POST":
        producto = request.form.get("producto")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")
        # Aquí puedes agregar la lógica para manejar el carrito de compras
        if producto in carrito_de_compras:
            carrito_de_compras[producto]['cantidad'] += int(cantidad)
        else:
            carrito_de_compras[producto] = {'cantidad': int(cantidad), 'precio': float(precio)}
    return redirect('/')

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    producto = request.form.get("producto")
    if producto and producto in carrito_de_compras:
        carrito_de_compras[producto]['cantidad'] -= 1
        if carrito_de_compras[producto]['cantidad'] <= 0:
            carrito_de_compras.pop(producto)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
