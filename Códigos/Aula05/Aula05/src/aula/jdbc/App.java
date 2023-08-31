package aula.jdbc;

public class App {
    public static void main(String[] args) throws Exception {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver carregado com sucesso!");
        } catch (Exception e) {
            System.out.println("Driver não pôde ser carregado...");
        }
    }
}
