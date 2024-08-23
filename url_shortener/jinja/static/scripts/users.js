function serializeForm(formNode) {
  return new FormData(formNode);
}

async function getData() {
  response = await fetch(window.location.origin + "/api/v1/users/", {
    method: "GET",
  });
  var data = await response.json();
  return data;
}

async function renderUser(user, userList) {
  var userDiv = document.createElement("div");
  userDiv.classList.add("accordion-item");
  userList.appendChild(userDiv);
  userDiv.insertAdjacentHTML(
    "beforeend",
    `
      <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${user["id"]}" aria-expanded="false" aria-controls="flush-collapseOne">
          ${user["username"]}
        </button>
      </h2>
    `
  );
  for (let url of user["shorted_urls"]) {
    userDiv.insertAdjacentHTML(
      "beforeend",
      `
      <div id="${
        user["id"]
      }" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
        ${window.location.origin + "/" + url["short_url_token"]} - ${
        url["full_url"]
      }
        </div>
      </div>
      `
    ); //
  }
}

async function renderUsersList() {
  const usersList = document.getElementById("users-list");
  const users = await getData();
  for (let user of users) {
    await renderUser(user, usersList);
  }
}

renderUsersList();
