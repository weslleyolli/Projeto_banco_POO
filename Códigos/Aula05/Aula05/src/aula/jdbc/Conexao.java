package aula.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao {
    public static void main(String[] args) {
        String driver = "com.mysql.cj.jdbc.Driver";
        String user = "root";
        String senha = "2045557732100asd";
        String url = "jdbc:mysql://localhost:3306/company?useSSL=false&serverTimezone=UTC";

        try {
            Class.forName(driver);
            Connection con = (Connection) DriverManager.getConnection(url, user, senha);
            System.out.println("Conexão realizada com sucesso");
        } catch (ClassNotFoundException e) {
            System.err.println("Driver JDBC não encontrado: " + e.getMessage());
        } catch (SQLException ex){
            System.err.println("Erro ao conectar ao banco de dados: " + ex.getMessage());
        }
        
    }
}