<h1>To-Do App API</h1>
<blockquote>To-Do App with Django and Django Rest Framework </blockquote>
<br>
<h2>How To-Do App Works?</h2>
<ul>
<li>A client can create a task.
<li>Each task can have a title, desription, priority, deadline and a mark shows if it is done (New Features to be Add).
<li>Client can edit or delete his/her older tasks.
</ul>
<h2>Installation</h2>
<ol>
<li><b>Get the code</b>
<p>Clone the repository<pre>git clone https://github.com/vuralmert/restfw-todo.git</pre></p>
<li><b>Install the project dependencies</b>
<p>Enter the following command<pre>pip install -r requirements.txt</pre></p>
<li><b>Run the commands to generate the database</b>
<p>Enter the following commands<pre>python manage.py makemigrations</pre><pre>python manage.py migrate</pre></p></ol>
<h2>Usage</h2>
<p>Once you have complete dowloading requirements and migrating and none of the services failed after you have run the following command,<pre>python manage.py runserver</pre>
<ol>
<li><b>Access and Interact with API Front-end App (Django Rest Framework)</b></li>
<p>The API Front-end application should be running and you can see it via your web browser at <a href="http://127.0.0.1:8000/todo/"></a>http://127.0.0.1:8000/todo which will take you to the main web app interface where you can create your tasks.</p>
<p>For the developers I created a Swagger UI which you can access it via your web browser at  <a href="http://127.0.0.1:8000/schema/swagger-ui/"></a>http://127.0.0.1:8000/schema/swagger-ui which will take you to the page that you can see all of your apis and schemas.</p>
<p>If you desire you can use <a href="http://127.0.0.1:8000/schema//"></a>http://127.0.0.1:8000/schema for downloading those apis as a .yaml file or <a href="http://127.0.0.1:8000/schema/redoc/"></a>http://127.0.0.1:8000/schema/redoc to edit your Swagger interface.</p>
<li><b>Access Django Admin</b></li>
<ol>
<li>Create the admin user</li>
<p>To access the admin interface first you gonna need to generate a super-user with the following command<pre>python manage.py createsuperuser</pre>You will be prompted to add a <code>username</code> and <code>password</code> for your user.<br></br>
<li>Logging to admin interface</li>
<p>Once you have complete creating the super-user you can visit <a href="http://127.0.0.1:8000/admin/"></a>http://127.0.0.1:8000/admin which will take you to the admin interface login screen. You should enter the <code>username</code> and <code>password</code> created in the previous step.
</ol></ol>
<h2>Endpoints</h2>
<ul>
<li><code>GET     /todo</code>
<li><code>POST    /todo</code>
<li><code>GET     /todo/{id}</code>
<li><code>PUT     /todo/{id}</code>
<li><code>DELETE  /todo/{id}</code>
</ul>
<h2>Used Techonologies</h2>
<ul>
<li>Python
<li>Django
<li>Django Rest Framework
</ul>
