
# Imports
import view_category as category

category_list = [
    '(acr) acreedores ',
    '(act) activos ',
    '(ban) bancos ',
    '(bil) billpayment ',
    '(con) contabilidad ',
    '(deu) deudores ',
    '(doc) doc_personales ',
    '(edu) educacion ',
    '(emp) empresas ',
    '(est) estrategia ',
    '(fid) fideicomisos ',
    '(fil) filantropia ',
    '(imp) impuestos',
    '(inm) inmuebles ',
    '(inv) inversiones ',
    '(pre) presupuesto ',
    '(pro) proyectos ',
    '(sal) salud',
    '(segd) seguridad ',
    '(segs) seguros ',
    '(ser) servicios ',
    '(suc) sucesion ',
]

def check_category():
    while True:
        category_search = input(
            ("\nSelect category. Type 'ls' for a list of categories or 'exit' to quit: "))
        if category_search == "ls":
            for item in category_list:
                print("    ", item)
            print("When finished, type 'exit' to quit.")

        elif category_search == "acr":
            category.acreedores()
        
        elif category_search == "act":
            category.activos()
        
        elif category_search == "ban":
            category.bancos()
        
        elif category_search == "bil":
            category.billpayment()
        
        elif category_search == "con":
            category.contabilidad()
        
        elif category_search == "deu":
            category.deudores()
        
        elif category_search == "doc":
            category.doc_personales()
        
        elif category_search == "edu":
            category.educacion()
        
        elif category_search == "emp":
            category.empresas()
        
        elif category_search == "est":
            category.estrategia()
        
        elif category_search == "fid":
            category.fideicomisos()

        elif category_search == "fil":
            category.filantropia()

        elif category_search == "imp":
            category.impuestos()

        elif category_search == "inm":
            category.inmuebles()

        elif category_search == "inv":
            category.inversiones()

        elif category_search == "pre":
            category.presupuesto()

        elif category_search == "pro":
            category.proyectos()

        elif category_search == "sal":
            category.salud()

        elif category_search == "segd":
            category.seguridad()

        elif category_search == "segs":
            category.seguros()

        elif category_search == "ser":
            category.servicios()

        elif category_search == "suc":
            category.sucesion()
            
        elif category_search == "exit":
            break

        else:
            print("Unrecognized category. Try again.")


if __name__ == "__main__":
    check_category()
