public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; // Inferencia de tipos
        while (conteo < 3) {
            System.out.println("conteo = " + conteo);
            conteo++;// Vamos aumentando en uno la variable
        }

        var contador = 0;
        do {
            System.out.println(("contador = " + contador));
            contador++;

        } while (contador < 7);

        for (var contando = 0; contador < 7; contador++) {
            if (contando % 2 == 0) {
                System.out.println("contando =" + contando);
                break;
            }
        }
        for (var contando = 0; contador < 7; contador++) {
            if (contando % 2 == 1) {
                continue; //Vamos a la siguiente iteración
            }
            System.out.println("contando =" + contando);
        }
    }
    }
}
