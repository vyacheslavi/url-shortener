function serializeForm(formNode) {
  return new FormData(formNode);
}

async function sendData(data) {
  return await fetch(window.location.origin + "/api/v1/tokens/", {
    method: "POST",
    body: data,
  });
}

async function handleFormSubmit(event) {
  event.preventDefault();
  // const button = (document.getElementById("btn").disabled = true);
  const fbck = document.getElementById("invalid-fbck");
  fbck.classList.add("d-none");
  shortURL = document.getElementById("shortURL");
  const data = serializeForm(applicantForm);
  console.log(data.json);
  const response = await sendData(data);
  if (response.ok) {
    shortURL.classList.remove("d-none");
    tokenURL = await response.json();
    shortURL.value = window.location.origin + "/" + tokenURL.short_url_token;
  } else {
    fbck.classList.remove("d-none");
    await response.json().then((err) => {
      fbck.innerHTML = Object.values(err)[0];
    });
  }
}

const applicantForm = document.getElementById("tokenURLForm");
applicantForm.addEventListener("submit", handleFormSubmit);
