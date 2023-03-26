function ready(fn) {
  if (typeof fn !== "function") {
    throw new Error("Argument passed to ready should be a function");
  }

  if (document.readyState != "loading") {
    fn();
  } else if (document.addEventListener) {
    document.addEventListener("DOMContentLoaded", fn, {
      once: true,
    });
  } else {
    document.attachEvent("onreadystatechange", function () {
      if (document.readyState != "loading") fn();
    });
  }
}

function getData(url, page, successFunc, element = window) {
  if (page) {
    var page = parseInt(page);
  } else {
    var page = 1;
  }
  var empty_page = false;
  var block_request = false;
  var connect = true;
  element.onscroll = function () {
    if (element === window) {
      var margin =
        document.documentElement.scrollHeight - window.innerHeight - 500;
      var scroll = window.scrollY;
    } else {
      var margin = element.scrollHeight - element.scrollTop - 200;
      var scroll = element.offsetHeight;
    }
    // console.log(margin)
    if (scroll > margin && empty_page == false && block_request == false) {
      block_request = true;
      if (connect) {
        page += 1;
      }
      var request = new XMLHttpRequest();
      request.onreadystatechange = function () {
        if (
          connect == false &&
          (this.readyState == 2 || this.readyState == 3)
        ) {
          connect = true;
          document.getElementById("connection-error").hidden = true;
        }
        if (this.readyState == 4 && this.status == 200) {
          var response = this.responseText;
          successFunc(response);
          block_request = false;
        } else if (this.readyState == 4 && this.status == 404) {
          empty_page = true;
          block_request = true;
        }
      };
      request.onerror = function () {
        document.getElementById("connection-error").hidden = false;
        connect = false;
        block_request = false;
      };
      request.open("GET", url + page, true);
      request.setRequestHeader("x-requested-with", "XMLHttpRequest");
      request.send();
    }
  };
}
