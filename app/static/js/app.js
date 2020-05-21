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
                <router-link class="nav-link" to="/register">Sign-Up</router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/explore">Explore</router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/posts/new">Make post</router-link>
              </li>
              <li class="nav-item active">
                <router-link class="nav-link" to="/logout">Logout</router-link>
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
      <div class="container-one">
        <img src="../static/uploads/bridge.jpg">
      </div>
      <div class="container-two">
          <h2><i class="fa fa-camera"></i>Photogram</h2>
          <hr>
          <p> Share photos of your favourite moments with friends
              family and the world</p>
          <button @click="$router.push('register')" type="button" name="button" class="green">Register</button>
          <button @click="$router.push('login')" type="button" name="button" class="blue">Login</button>
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
        <h1>Register</h1>
        <hr>
        <p>Please fill out all fields listed below.</p>
        <form @submit.prevent="signUp" id="signUpForm" method="post" enctype="multipart/form-data">

          <div class="form-group">
            <label for="firstname"> First Name </label>
            <input type="text" name="firstname" placeholder="First Name">
          </div>

          <div class="form-group">
            <label for="lastname"> Last Name </label>
            <input type="text" name="lastname" placeholder="Last Name">
          </div>

          <div class="form-group">
            <label for="username"> Username </label>
            <input type="text" name="username" placeholder="Username">
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
            <label for="password"> Password </label>
            <input type="password" name="password" >
          </div>

          <div class="form-group">
            <label for="location"> Location </label>
            <input type="text" name="location" placeholder="Where are you from?">
          </div>

          <div class="form-group bio" id="t-area">
            <label for="bio"> Biography</label>
            <input type="text" name="bio" placeholder="Tell us about you">
          </div>

          <div class="form-group">
            <label for="photo"> Profile Photo </label>
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
            console.log(" Sign up function runs")
            let self = this;
            let signUpForm = document.getElementById('signUpForm');
            let form_data = new FormData(signUpForm);

            fetch("/api/users/register", {
                method: 'POST',
                body: form_data,
                headers: {

                },
                credentials: 'same-origin'
            })
            .then(function (response){
                return response.json();
            })
            .then(function (jsonResponse) {
                console.log(jsonResponse);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
});

const Login = Vue.component('login',{
    template:`
      <div>

        <form class="form-login" @submit.prevent="loginUser" id="loginForm" method="post" enctype="multipart/form-data">
          <h2>Login</h2>
          <hr>
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
          <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
        </form>
      </div>
    `,
    data: function () {
        return {
            error: "None",
            message: ""
        }
    },
    created: function () {
      console.log("Entered the login page");
    },
    methods: {
        loginUser: function(){
            console.log("Login function runs")
            let self = this;
            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);

            fetch("/api/auth/login", {
                method: 'POST',
                body: form_data,
                headers: {

                },
                credentials: 'same-origin'
            })
            .then(function (response){
                return response.json();
            })
            .then(function (response) {
                let jwt_token = response.status.token;
                let message = response.status.message;

                console.log(message);
                localStorage.setItem('token', jwt_token);
                console.info('Token generated and added to localStorage');
                if (jwt_token) {
                    router.push('explore');
                } else {
                    console.log("reloading router..");
                    router.go()
                }
            })
            .then(function (jsonResponse) {

              console.log(jsonResponse);
            })
            .catch(function (error) {
                console.log(error);
                error = error
            });
        },

    }
});

const Logout = Vue.component('logout',{
    template:`
        <div>
        <h2> You have been successfully logged out </h2>
        <button @click="$router.push('/')"> Return to home </button>
        </div>
    `,
    created: function() {
        fetch('/api/auth/logout',{
          method: 'GET',
          headers: {
              Authorization: 'Bearer ' + localStorage.getItem('token')
          }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (jsonResponse) {
            localStorage.removeItem('token');
            console.log('Token removed from localStorage')
            console.log(jsonResponse);
        })
        .catch(function (error) {
            console.log(error);
        });
    },
    data: function () {
        return {
            message: ''
        }
    },
    methods: {
    }
});

const Explore = Vue.component('explore',{
    template: `
        <div class="posts">
          <button type="button" name="button" class="make-posts" >Make Post</button>

          <!-- code to display the posts and select component by id-->

          <ul  v-if="posts === '' ">
              <h2> No posts to display....or you arent authorized</h2>
          </ul>

          <ul v-else class="disp-all">
              <li v-for="post in posts" class="each-post">
                  <div class="headss">
                  <img class="small" :src="'/static/uploads/' + post.user_photo">
                  <h4> {{ post.created_by }} </h4>
                  </div>
                  <img :src="'static/uploads/' + post.photo" />
                  <h6> {{ post.caption }} </h6>
                  <p><i class="fas fa-heart"></i>Likes</p>
                  <i class="far fa-heart"></i>
                  <p class="datetime"> {{ post.created_on }}</p>
              </li>
          </ul>

        </div>
    `,
    created: function () {
      //do something after creating vue instance
      let self = this;
      console.log("Vue instance created");

      fetch("/api/posts", {
          method: 'GET',
          headers: {
              'Authorization': 'Bearer ' + localStorage.getItem('token')
          }
      })
      .then(function (response) {
          return response.json();
      })
      .then(function (data) {
          if (data.posts) {
              console.log(data.posts);
              self.posts = data.posts;
          } else {
            console.log("error getting posts")
          }
      })
      .catch(function (error) {
        self.result = `There was an error`;
          console.log(self.result);
      })
    },
    data: function (){
        return {
          posts : []
        }
    },
    methods:{
      // getPost:function () {
      //
      //     let self = this;
      //
      //     fetch("/api/posts", {
      //         method: 'GET',
      //         'headers': {
      //             'Authorization': 'Basic ' + localStorage.getItem('token')
      //         }
      //     })
      //     .then(function (response) {
      //         return response.json();
      //     })
      //     .then(function (response) {
      //         //console.log(jsonResponse);
      //
      //         if (response.data) {
      //             let result = response.data;
      //
      //             self.result = `It works!!`;
      //             console.log(self.result);
      //         } else {
      //             self.result = `Neva work ennuh G`;
      //             console.log(self.result);
      //         }
      //     })
      //     .catch(function (error) {
      //       self.result = `There was an error`;
      //         console.log(self.result);
      //     })
      // }
    }
});

const MakePost = Vue.component('make-post',{
    template:`

    <div class="new_">
    <h3>New Post</h3>
    <hr>
      <form @submit.prevent="makePost" id="postForm" method="post" enctype="multipart/form-data">
        <div class="form-group">
        <label for="photopost"> Photo </label>
        <input class="photopost" type="file" name="photopost" id="photopost" value="Put Image Here"><br />
        </div>

        <div class="form-group">
        <label for="description"> Caption </label>
        <input type="text" name="description" id="description" value="" class="caption" placeholder="Write a caption...">
        </div>

        <button type="submit"> Submit </button>
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

          fetch("/api/users/<user_id>/posts", {
              method: 'POST',
              body: form_data,
              headers:{},
              credentials: 'same-origin'
          })
          .then(function (response) {
              return response.json();
          })
          .then(function (jsonResponse) {
              console.log(jsonResponse);
          })
          .catch(function (error) {
              console.log(error);
          });
      }
    }
});

const ViewUser = Vue.component('view-user',{
    template:`
    <div>
      <div class="prosplash">
          <div class="lead">
            <img :src="'/static/uploads/' + user.photo">
          </div>
          <div class="who">
            <h3 class="head">{{user.firstname}} {{user.lastname}}</h3>
            <ul class="oinfo">
              <li class="rrm where">{{ user.location }}</li>
              <li class="rrm when">Joined on {{ user.joindate }}</li>
              <li class="rrm email">{{ user.biography }}</li>
            </ul>
          </div>
          <div class="flls">
          <ul>
            <li class="ind"> Posts: {{ user.posts }} </li>
            <li class="ind"> Followers: {{ user.followers }} </li>
            <button>Follow</button>
          </ul>
          </div>
      </div>
        <div class="flx-container">
          <ul class="rrm">
            <li v-for="post in posts"><img :src="'/static/uploads/' + post.photo"></li>
          </ul>
        </div>
    </div>
    `,
    created: function() {
      let self = this;
      //do something after creating vue instance
      fetch("/api/users/" + this.$route.params.user_id + "/posts",{
          method: 'GET',
          headers: {},
          credentials: 'same-origin'
      })
      .then(function (response) {
          return response.json();
      })
      .then(function (response) {
          if (response.data) {
              console.log(response.data.posts);
              console.log(response.data.user);
              self.posts = response.data.posts;
              self.user = response.data.user;
          }else{
              console.log("error getting posts")
          }
      })
      .then(function (jsonResponse) {

      })
      .catch(function (error) {
          console.log('There was an error');
      })
    },
    data: function (){
        return {
            posts: [],
            user: []
        }
    },
    methods: {
      followUser: function() {
          fetch("/api/users/"+ self.user.id + "follow",{
              method: 'GET',
              headers: {

              },
              credentials: 'same-origin'
          })
          .then(function (response) {
              return response.json();
          })
          .then(function (jsonResponse) {
            console.log(jsonResponse);
          })
          .catch(function (error) {
              console.log(error);
          })

      }
    }
})

const router = new VueRouter({
  mode: 'history',
  routes: [
      { path: '/', component: Home },
      { path: '/register', component: SignUp },
      { path: '/About', component: About },
      { path: '/login', component: Login },
      { path: '/logout', component: Logout },
      { path: '/explore', component: Explore },
      { path: '/posts/new', component: MakePost },
      { path: '/users/:user_id', component: ViewUser}
  ]
})

// Instantiating main vue instance
let app = new Vue({
    el: "#app",
    router,
    data: {
        token: '',
    }
});
