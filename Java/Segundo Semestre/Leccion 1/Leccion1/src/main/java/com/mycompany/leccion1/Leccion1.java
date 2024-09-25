
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos01 {

    public static void main(String[] args) {
        int numero, cuadrado;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite el número: "));
        while (numero >= 0) { // Mientras el número sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero " + numero + "elevado al  cuadrado es: " + cuadrado);
            System.out.println("Digite otro  numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}
