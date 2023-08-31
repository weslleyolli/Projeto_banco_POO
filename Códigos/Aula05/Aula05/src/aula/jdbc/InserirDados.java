package aula.jdbc;

import javax.swing.*;
import java.awt.*;
import java.sql.*;

public class InserirDados extends JFrame {
	private Connection con;
	private Statement st;

	public InserirDados(){
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

		try{
			st = con.createStatement();
			st.executeUpdate("INSERT INTO tabelaTeste values(1, 'Felipe')");
			JOptionPane.showMessageDialog(this,"Dados inseridos com sucesso!","Mensagem", JOptionPane.WARNING_MESSAGE);
		}catch (SQLException eSQL) {
			eSQL.printStackTrace();
			JOptionPane.showMessageDialog(this,"Não foi possível inserir valores na tabela!\n" + "Mensagem: " + eSQL.getMessage(),"Erro", JOptionPane.ERROR_MESSAGE);
			System.exit(2);
		}
		
		try {
			st.close();
			con.close();
		}catch(Exception exception){
			exception.printStackTrace();
			System.exit(2);
		}
		Container P = getContentPane();
		P.setLayout(new FlowLayout());
		JLabel mensagem = new JLabel("Você acabou de testar um exemplo usando INSERT!");
		P.add(mensagem);
	}

	
	public static void main(String args[]){
		InserirDados ex = new InserirDados();
		ex.setDefaultCloseOperation(EXIT_ON_CLOSE);
		ex.setTitle("USANDO INSERT");
		ex.setVisible(true);
		ex.setSize(400,200);
	}
	
}