Paso nro 1: crear archivo forms.py dentro de la aplicación.
    Contiene la importación de forms desde django y a partir de ahí todo debe tener el formato 
    class xxxx(forms.Form).

Paso nro 2.1: Importar de .forms todo. 
Paso nro 2.2: crear una función que resuelva todo el formulario.
    - Si request.method == "POST" entonces no es la primera vez que se llena el formulario.
    - Si no es así, entonces entra en el else.
Paso nro 2.3: Si estoy en la nsima vez que se llena el formulario se toman los datos del request.POST
Paso nro 3: Crear html con form.as_table que puede servir para cualquier clase formulario.
Paso nro 4: crear la ruta en urls.py