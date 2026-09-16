import re

# Paths
index_path = "index_backup.html"
css_path = "css/style.css"
js_path = "js/main.js"

# Read files
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Add free resource button to hero-buttons
# Find <div class="hero-buttons"> ... </div>
def add_free_resource_button(match):
    inner = match.group(1)
    # Insert button before closing </div>
    return inner + '\n          <a href="javascript:void(0);" class="btn btn-outline" id="freeResourceBtn">免费获取《5类企业债务重组常见误差及自查表》</a>'
html = re.sub(r'(<div class="hero-buttons">[\s\S]*?)(</div>)', add_free_resource_button, html, count=1)

# 2. Add modal before </body>
modal_html = '''<!-- 免费资源弹窗 -->
<div id="freeResourceModal" class="modal">
  <div class="modal-content">
    <span class="close" id="freeResourceClose">&times;</span>
    <h2>免费资源获取</h2>
    <p>请扫描下方二维码关注微信公众号，回复“债务重组”获取《5类企业债务重组常见误差及自查表》。</p>
    <img src="images/wechat-qr.png" alt="微信二维码" style="width:200px;height:200px;display:block;margin:0 auto;">
  </div>
</div>'''
html = re.sub(r'(</body>)', modal_html + r'\n\1', html, count=1)

# 3. Add service-link after each <p> inside .service-card
def add_service_link(match):
    return match.group(0) + '\n          <a href="#knowledge" class="service-link">查看相关操作指南</a>'
html = re.sub(r'(<p>[^<]*?</p>)', add_service_link, html)

# 4. Add knowledge center subscription form after .knowledge-grid closing </div>
def insert_subscription(match):
    return match.group(0) + '''
<!-- 知识中心订阅区 -->
<div class="knowledge-subscribe animate-on-scroll">
  <h3>订阅每周洞察</h3>
  <p>输入您的邮箱，获取债务重组最新政策、案例分析与实务工具。</p>
  <form id="subscribeForm" action="https://formspree.io/f/your_form_id" method="POST">
    <input type="email" name="email" placeholder="您的邮箱" required>
    <button type="submit" class="btn btn-primary">立即订阅</button>
  </form>
  <p style="margin-top:12px;font-size:0.9rem;color:#666;">
    我们承诺不泄漏您的信息，随时可退订。
  </p>
</div>'''
html = re.sub(r'(<div class="knowledge-grid">[\s\S]*?</div>)', insert_subscription, html, count=1)

# 5. Add footer WeChat link
def add_footer_wechat(match):
    return match.group(1) + '\n    <li>\n      <a href="javascript:void(0);" id="footerWechat">\n        添加微信获取免费资料 <img src="images/wechat-qr.png" alt="微信" style="width:16px;height:16px;vertical-align:middle;">\n      </a>\n    </li>\n' + match.group(2)
html = re.sub(r'(<div class="footer-col">[\s\S]*?<ul>[\s\S]*?)(</ul>)', add_footer_wechat, html, count=1)

# 6. Update contact form action
html = re.sub(r'(<form id="contactForm"[^>]*?)>', r'\1 action="https://formspree.io/f/your_form_id" method="POST">', html)

# 7. Add SEO meta and JSON-LD before </head>
seo_html = '''<!-- SEO 基础 -->
<meta name="robots" content="index,follow">
<meta name="author" content="平台化困境企业救治">
<link rel="canonical" href="https://您的域名.com/">
<!-- JSON-LD 结构化数据（LocalBusiness） -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "平台化困境企业救治",
  "image": "https://您的域名.com/images/wechat-qr.png",
  "@id": "https://您的域名.com/",
  "url": "https://您的域名.com/",
  "telephone": "13908373468",
  "priceRange": "请咨询",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "请填写具体地址",
    "addressLocality": "请填写城市",
    "postalCode": "请填写邮编",
    "addressCountry": "CN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "您的纬度",
    "longitude": "您的经度"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "sameAs": [
    "https://微信公众号链接",
    "https://其他社媒链接"
  ]
}
</script>'''
html = re.sub(r'(</head>)', seo_html + r'\n\1', html, count=1)

# Write modified index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 8. Append CSS for modal, service-link, knowledge-subscribe
css_add = '''

/* 免费资源弹窗样式 */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}
.modal-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
  text-align: center;
  position: relative;
}
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

/* 服务卡链接样式 */
.service-link {
  display: inline-block;
  margin-top: 12px;
  font-size: 0.9rem;
  color: #0066cc;
  text-decoration: none;
}
.service-link:hover {
  text-decoration: underline;
}

/* 知识中心订阅区 */
.knowledge-subscribe {
  background: #f8fbff;
  padding: 24px;
  border-radius: 8px;
  text-align: center;
}
.knowledge-subscribe input[type=email] {
  width: 100%;
  max-width: 360px;
  padding: 10px;
  margin: 12px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.knowledge-subscribe .btn {
  width: 100%;
  max-width: 360px;
}
'''
with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_add)

# 9. Append JS for modal, footer wechat link, form AJAX
js_add = '''

/* 免费资源弹窗交互 */
document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('freeResourceBtn');
  const modal = document.getElementById('freeResourceModal');
  const span = document.getElementById('freeResourceClose');

  btn.onclick = function () {
    modal.style.display = 'block';
  };
  span.onclick = function () {
    modal.style.display = 'none';
  };
  window.onclick = function (event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  };
});

/* 页脚微信链接打开同样弹窗 */
document.getElementById('footerWechat')?.addEventListener('click', function (e) {
  e.preventDefault();
  document.getElementById('freeResourceModal').style.display = 'block';
});

/* 联系表单 AJAX 提交 */
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault(); // 阻止默认跳转

    const submitBtn = form.querySelector('.btn-submit');
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span>提交中…</span>';
    submitBtn.disabled = true;

    const formData = new FormData(form);
    fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('网络错误');
    })
    .then(data => {
      // 成功提示
      submitBtn.innerHTML = '<span>提交成功！</span>';
      submitBtn.style.backgroundColor = '#28a745';
      # 5秒后恢复按钮状态（可选）
      setTimeout(() => {
        submitBtn.innerHTML = originalBtnText;
        submitBtn.style.backgroundColor = '';
        submitBtn.disabled = false;
        form.reset();
      }, 3000);
    })
    .catch(err => {
      # 错误提示
      submitBtn.innerHTML = '<span>提交失败，请重试</span>';
      submitBtn.style.backgroundColor = '#dc3545';
      setTimeout(() => {
        submitBtn.innerHTML = originalBtnText;
        submitBtn.style.backgroundColor = '';
        submitBtn.disabled = false;
      }, 3000);
      console.error(err);
    });
  });
});
'''
with open(js_path, "a", encoding="utf-8") as f:
    f.write(js_add)

print("Modification complete.")
