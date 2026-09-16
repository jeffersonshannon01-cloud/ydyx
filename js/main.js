// 平台化困境企业救治 - 网站交互脚本
const navbar = document.querySelector(".navbar");
window.addEventListener("scroll", () => { navbar.classList.toggle("scrolled", window.scrollY > 50); });
const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
const navLinks = document.querySelector(".nav-links");
if (mobileMenuBtn) { mobileMenuBtn.addEventListener("click", () => { navLinks.classList.toggle("active"); mobileMenuBtn.classList.toggle("active"); }); }
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) { target.scrollIntoView({ behavior: "smooth", block: "start" }); navLinks.classList.remove("active"); } 
  });
});
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add("visible"); });
}, { threshold: 0, rootMargin: "0px 0px 0px 0px" });
document.querySelectorAll(".animate-on-scroll").forEach(el => observer.observe(el));
const contactForm = document.getElementById("contactForm");
if (contactForm) {
  contactForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();
    if (!name || !phone) { alert("请填写姓名和手机号"); return; }
    const phoneRegex = /^1[3-9]\d{9}$/;
    if (!phoneRegex.test(phone)) { alert("请输入正确的手机号"); return; }
    const btn = this.querySelector(".btn-submit");
    btn.textContent = "提交中..."; btn.disabled = true;
    // Using fetch to Formspree (assuming action set)
    const formData = new FormData(form);
    fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: { 'Accept': 'application/json' }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('网络错误');
    })
    .then(data => {
      // 成功提示
      btn.innerHTML = '<span>提交成功！</span>';
      btn.style.backgroundColor = '#28a745';
      setTimeout(() => {
        btn.innerHTML = originalBtnText;
        btn.style.backgroundColor = '';
        btn.disabled = false;
        form.reset();
      }, 3000);
    })
    .catch(err => {
      // 错误提示
      btn.innerHTML = '<span>提交失败，请重试</span>';
      btn.style.backgroundColor = '#dc3545';
      setTimeout(() => {
        btn.innerHTML = originalBtnText;
        btn.style.backgroundColor = '';
        btn.disabled = false;
      }, 3000);
      console.error(err);
    });
  });
}
function animateNumbers() {
  document.querySelectorAll(".stat-card .number").forEach(num => {
    const target = parseInt(num.textContent.replace(/[^0-9]/g, ""));
    const suffix = num.textContent.replace(/[0-9]/g, "");
    let current = 0; const increment = target / 50;
    const timer = setInterval(() => { current += increment; if (current >= target) { num.textContent = target + suffix; clearInterval(timer); } else { num.textContent = Math.floor(current) + suffix; } }, 30);
  });
}
window.addEventListener("load", () => { const heroStats = document.querySelector(".hero-stats"); if (heroStats) setTimeout(animateNumbers, 500); });
// 滚动显示回到顶部
const topBtn = document.querySelector('.float-btn.top');
window.addEventListener('scroll', () => {
  if (topBtn) topBtn.classList.toggle('show', window.scrollY > 400); 
});
topBtn && topBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
// 倒计时：当天 23:59:59 结束
function startCountdown() {
  const el = document.getElementById('countdown');
  if (!el) return;
  const target = new Date();
  target.setHours(23,59,59,999);
  function update() {
    const now = new Date();
    const diff = target - now;
    if (diff <= 0) { el.textContent = '名额已抢完'; return; }
    const h = Math.floor(diff / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    el.textContent = h + '时' + m + '分' + s + '秒';
  }
  update();
  setInterval(update, 1000);
}
startCountdown();
// 免费资源弹窗交互
document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('freeResourceBtn');
  const modal = document.getElementById('freeResourceModal');
  const span = document.getElementById('freeResourceClose');
  btn.onclick = function () { modal.style.display = 'block'; };
  span.onclick = function () { modal.style.display = 'none'; };
  window.onclick = function (event) { if (event.target === modal) { modal.style.display = 'none'; } };
});
// 页脚微信链接打开同样弹窗
document.getElementById('footerWechat')?.addEventListener('click', function (e) {
  e.preventDefault();
  document.getElementById('freeResourceModal').style.display = 'block';
});
