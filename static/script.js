const socket = io();

socket.on('new_message', (data) => {
  const ul = document.getElementById('messages');
  const li = document.createElement('li');
  li.textContent = data.content;
  ul.prepend(li);
});

// ページロード時に過去メッセージ取得
window.onload = async () => {
  const res = await fetch('/messages');
  const messages = await res.json();
  const ul = document.getElementById('messages');
  messages.forEach((msg) => {
    const li = document.createElement('li');
    li.textContent = msg.content;
    ul.appendChild(li);
  });
};
