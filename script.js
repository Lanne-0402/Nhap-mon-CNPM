document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Ngăn form submit mặc định

  let username = document.getElementById("username").value.trim();
  let password = document.getElementById("password").value.trim();
  let message = document.getElementById("message");

  if (username === "" || password === "") {
    message.textContent = "⚠️ Vui lòng nhập đầy đủ Username và Password!";
    return;
  }

  // Kiểm tra đơn giản (có thể thay bằng gọi API thực tế)
  if (username === "baodiep" && password === "050105") {
    message.style.color = "green";
    message.textContent = "✅ Đăng nhập thành công!";
  } else {
    message.style.color = "red";
    message.textContent = "❌ Sai Username hoặc Password!";
  }
});

function cancelLogin() {
  document.getElementById("loginForm").reset();
  document.getElementById("message").textContent = "";
}
