package aula_01;

import java.io.FileWriter;
import java.io.IOException;

public class PersistenciaCSV {
    public static void main(String[] args) {
        String csvFile = "dados.csv";
        try {
            FileWriter writer = new FileWriter(csvFile);

            writer.append("Usuário,Senha\n");

            writer.append("João,Secreta\n");

            writer.flush();
            writer.close();

            System.out.println("Arquivo CSV criado com sucesso!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}