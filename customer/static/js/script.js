function validateForm() {
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        var errorMessage = document.getElementById('error-message');
      
        if (email === '' || password === '') {
          errorMessage.innerHTML = 'Please enter your email and password.';
          return false;
        } else {
          errorMessage.innerHTML = '';
          return true;
        }
      }
      