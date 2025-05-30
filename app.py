from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

carrito_de_compras = {}

@app.route("/", methods=["GET", "POST"])

def index():
    total = sum(info['cantidad'] * info['precio'] for info in carrito_de_compras.values())
    mostrar_grafica = request.args.get('grafica') == '1'
    imagen_grafica = generar_grafica() if mostrar_grafica else None
    return render_template("index.html", carrito=carrito_de_compras, total_pro=total, imagen_grafica=imagen_grafica)


def generar_grafica():
    if not carrito_de_compras:
        return None
        #return "<p>No hay productos en el carrito para graficar.</p>"

    productos = list(carrito_de_compras.keys())
    cantidades = [info["cantidad"] for info in carrito_de_compras.values()]

    fig, ax = plt.subplots()
    ax.bar(productos, cantidades, color="lightcoral")
    ax.set_title("Carrito de Compras")
    ax.set_ylabel("Cantidad")
    ax.set_xlabel("Producto")
    plt.xticks(rotation=45, ha="right")

    buffer = io.BytesIO()
    plt.tight_layout()
    fig.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)

    grafica_barras = base64.b64encode(buffer.read()).decode("utf-8")
    return grafica_barras



@app.route("/carrito", methods=["GET", "POST"])
def carrito():
    if request.method == "POST":
        producto = request.form.get("producto")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")
        # Aquí puedes agregar la lógica para manejar el carrito de compras
        if producto in carrito_de_compras:
            carrito_de_compras[producto]["cantidad"] += int(cantidad)
        else:
            carrito_de_compras[producto] = {"cantidad": int(cantidad), "precio": float(precio)}
    return redirect("/")

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    producto = request.form.get("producto")
    if producto and producto in carrito_de_compras:
        carrito_de_compras[producto]["cantidad"] -= 1
        if carrito_de_compras[producto]["cantidad"] <= 0:
            carrito_de_compras.pop(producto)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
