package aula.jdbc;

import javax.swing.*;
import java.awt.*;
import java.sql.*;

public class Atividade extends JFrame {
	private Connection con;
	private Statement st;

	public Atividade(){
		String driver = "com.mysql.cj.jdbc.Driver";
        String sUsuario = "root";
        String sSenha = "2045557732100asd";
        String sFonte = "jdbc:mysql://localhost:3306/JavaTest?useSSL=false&serverTimezone=UTC";

		try {
			Class.forName(driver);
			con = DriverManager.getConnection(sFonte, sUsuario, sSenha);
			JOptionPane.showMessageDialog(this,"Banco conectado com sucesso!","Mensagem", JOptionPane.WARNING_MESSAGE);

		}catch (SQLException eSQL) {
			// exceções de SQL
			eSQL.printStackTrace();
			JOptionPane.showMessageDialog(this,"Falha na conexão com o banco!\nMensagem: " + eSQL.getMessage(),"Erro", JOptionPane.ERROR_MESSAGE);
			System.exit(0);
		}catch (Exception e) {
			// demais exceções
			e.printStackTrace();
			JOptionPane.showMessageDialog(this,"Falha na conexão com o banco!\nMensagem: " + e.getMessage(),"Erro", JOptionPane.ERROR_MESSAGE);
			System.exit(1);
		}
		
		String sentencaSQL = "CREATE TABLE Loja (codProduto INT, produto VARCHAR(50), constraint pk_Teste primary key(codProduto));";

        String insercaoString = "Insert into Loja (codProduto, produto) VALUES (1, 'Arroz'), (2, 'Feijão'), (3, 'Macarrão')";

		try{
			st = con.createStatement();
			st.executeUpdate(sentencaSQL);
            st.executeUpdate(insercaoString);
			JOptionPane.showMessageDialog(this,"Tabela criada e dados adicionados com sucesso!","Mensagem", JOptionPane.WARNING_MESSAGE);
		}catch (SQLException eSQL) {
			eSQL.printStackTrace();
			JOptionPane.showMessageDialog(this,"Não foi possível criar a tabela!\n" + "Mensagem: " + eSQL.getMessage(),"Erro", JOptionPane.ERROR_MESSAGE);
			System.exit(2);
		}
		
		try {
			st.close();
			con.close();
		}catch(Exception exception){
			exception.printStackTrace();
			System.exit(3);
		}
		Container P = getContentPane();
		P.setLayout(new FlowLayout());
		JLabel mensagem = new JLabel("Você acabou de testar um exemplo usando CREATE TABLE!");
		P.add(mensagem);
	}

	
	public static void main(String args[]){
		Atividade ex = new Atividade();
		ex.setDefaultCloseOperation(EXIT_ON_CLOSE);
		ex.setTitle("Atividade finalizada");
		ex.setVisible(true);
		ex.setSize(400,300);
	}
	
}