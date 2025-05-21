from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("index.html")

def carrito_de_compras():
    if request.method == "POST":
        producto = request.form.get("producto")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")
        # Aquí puedes agregar la lógica para manejar el carrito de compras
        return f"Producto: {producto}, Cantidad: {cantidad}, Precio: {precio}"
    return render_template("carrito_de_compras.html")


if __name__ == "__main__":
    app.run(debug=True)
