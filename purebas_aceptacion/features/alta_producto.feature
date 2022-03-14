Característica: Alta producto
    Como usuario de la plataforma comercial digital
    Deseo iniciar sesion como empresa
    Para poder dar de alta un producto

    Escenario: Alta de producto como empresa
            Dado que ingreso al sistema con credenciales correctas,
            Cuando doy click en "Iniciar Sesión"
            Y ingreso el nombre con "usuario_prueba_empresa2"
            Y ingreso la contraseña con "prueba123"
            Y presiono el botón "Ingresar"
            Entonces ingreso a la pantalla de inicio
            Cuando doy click en "Administrar Productos"
            Y doy click en el boton "Nuevo Producto"
            Entonces ingreso el vendedor
            Y ingreso el nombre "Cinto"
            Y el precio "10"
            Y el stock "50"
            Y la categoria "Talabarteria"
            Y una descripcion "Cinto perforado"
            Y presiono el boton de "Agregar"
            Entonces me redirije a la pantalla de lista de articulos
