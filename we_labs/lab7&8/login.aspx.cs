using System;
using System.Web.UI;

public partial class Login : Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
    }

    protected void btnLogin_Click(object sender, EventArgs e)
    {
        if (Page.IsValid)
        {
            string username = txtUsername.Text;
            string password = txtPassword.Text;


            if (username == "admin" && password == "password123")
            {
                Response.Redirect("HomePage.aspx");
            }
            else
            {
                ClientScript.RegisterStartupScript(this.GetType(), "alert", "alert('Invalid username or password.');", true);
            }
        }
    }
}
