/* Add your Application JavaScript */
Vue.component('app-header',{
    template:`
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
          <span class="navbar-brand mb-0 h1">Photogram</span>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/about">About</router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/profile">Sign-Up</router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/posts">Posts</router-link>
              </li>
            </ul>
          </div>
        </nav>
    </header>
    `
});

Vue.component('app-footer',{
    template:`
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});

const Home = Vue.component('home',{
    template: `
    <div class="noted">
      <div class="container">
        <h1>Hello, world!</h1>
        <p>This is 620103170's submission of INFO3180 project 1</p>
        <p><a class="btn btn-primary" href="#" role="button">Learn more »</a></p>
      </div>
      <div class="container">
          <h2>Photogram</h2>
          <p> Share photos of your favourite moments with friends
              family and the world</p>
          <button @click="$router.push('register')" type="button" name="button">Register</button>
          <button @click="$router.push('login')" type="button" name="button">Login</button>
      </div>
    </div>
    `,
    data: function() {
        return {}
    }
});

const About = Vue.component('about',{
    template:`
        <div>
          <h1> About us </h1>
          <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit,
          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
          voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum.
          </p>
          <div>
            <h2>Contact Us</h2>
            <form>
            </form>
          </div>
        </div>
    `,
    data: function () {
        return {}
    }
});

const SignUp = Vue.component('signup',{
    template:`
      <div class="sign">
        <h1>Profile - Sign Up</h1>
        <p>Please fill out all fields listed below.</p>
        <form @submit.prevent="signUp" id="signUpForm" method="post" enctype="multipart/form-data">

          <div class="form-group">
            <label for="firstname"> First Name: </label>
            <input type="text" name="firstname" placeholder="First Name">
          </div>

          <div class="form-group">
            <label for="lastname"> Last Name: </label>
            <input type="text" name="lastname" placeholder="Last Name">
          </div>

          <div class="form-group">
            <label for="gender"> Gender </label>
            <input type="text" name="gender" placeholder="Gender">
          </div>

          <div class="form-group">
            <label for="email"> Email </label>
            <input type="text" name="email" placeholder="example@test.com">
          </div>

          <div class="form-group">
            <label for="location"> Location: </label>
            <input type="text" name="location" placeholder="Where are you from?">
          </div>

          <div class="form-group" id="t-area">
            <label for="bio"> Biography</label>
            <input type="text" name="bio" placeholder="Tell us about you">
          </div>

          <div class="form-group">
            <label for="photo"> Profile Photo: </label>
            <input type="file" name="photo" placeholder="Upload a photo">
          </div>

          <button type="submit">Submit</button>
        </form>
      </div>
    `,
    data: function () {
        return {}
    },
    methods: {
        signUp: function() {
            let self = this;
            let signUpForm = document.getElementById('signUpForm');
            let form_data = new FormData(signUpForm);
        }
    }
});

const Login = Vue.component('login',{
    template:`
    <div>
      <form class="form-login" @submit.prevent="loginUser" id="loginForm" method="post" enctype="multipart/form-data">
        <h2>Please Log in</h2>

          <div v-if="error != 'None' " class="alert alert-danger">
            <strong>Error:</strong> <$ error $>
          </div>
        <div class="form-group">
          <label for="username" class="sr-only">Username</label>
          <input type="text" id="username" name="username" class="form-control" placeholder="Your username" required >
        </div>
        <div class="form-group">
          <label for="password" class="sr-only">Password</label>
          <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>
    </div>
    `,
    data: function () {
        return { error : "None" }
    },
    methods: {
        loginUser: function(){
            let self = this;
            let loginForm = document.getElementById('loginForm')
            let form_data = new FormData(loginForm);
        }
    }

})

/*const Logout = Vue.component('logout',{
});*/

const Explore = Vue.component('posts',{
    template: `
        <div>
          <h1>Return all Posts..</h1>
          <!-- code to display the posts and select component by id-->
        </div>
    `,
    data: function (){
        return {}
    },
    methods:{
      getPost:function () {

      }
    }
});

const MakePost = Vue.component('make-post',{
    template:`
    <div>
      <form @submit.prevent="makePost" id="makePost" method="post" enctype="multipart/form-data">

        <label for="description"> Description: </label>
        <input type="text" name="description" id="description" value="">

        <label for="photofile"> Pic: </label>
        <input type="file" name="photofile" id="photofile" value="Put Image Here"><br />

        <input type="submit" value="Submit">
      </form>
    </div>
    `,
    data: function () {
        return {}
    },
    methods: {
      makePost: function() {
          let self = this;
          let postForm = document.getElementById('postForm');
          let form_data = new FormData(postForm);



      }
    }
});



const router = new VueRouter({
  mode: 'history',
  routes: [
      { path: '/', component: Home },
      { path: '/register', component: SignUp },
      { path: '/About', component: About },
      { path: '/login', component: Login },
      //{ path: '/logout', component: Logout },
      { path: '/explore', component: Explore },
      { path: '/profile', component: SignUp },
      { path: '/posts/new', component: MakePost },
      //{ path: '/users/:user_id', component: ViewUser}
  ]
})
// Instantiating main vue instance
let app = new Vue({
    el: "#app",
    router
});
