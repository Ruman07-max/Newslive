// ================= API CONFIG =================
const API_BASE_URL = 'http://localhost:8000/api';
let currentCategory = 'home';

// ================= INIT =================
document.addEventListener('DOMContentLoaded', () => {
  setCurrentDate();
  loadCategories();

  const page = window.location.pathname.split('/').pop();
  if (page === '' || page === '/' || page === 'index.html') {
    loadTopHeadlines();
    loadEpaper();
    loadLatestNews();
    setupCategoryTabs();
  } else if (page === 'category.html') {
    loadCategoryPage();
    loadEpaper();
    loadLatestNews();
  } else if (page === 'news-detail.html') {
    loadNewsDetail();
    loadRelatedNews();
  }

  setupMobileMenu();
});

// ================= HELPERS =================
async function fetchData(endpoint) {
  const res = await fetch(`${API_BASE_URL}${endpoint}`);
  if (!res.ok) throw new Error('API Error');
  return await res.json();
}

function setCurrentDate() {
  const el = document.getElementById('current-date');
  if (!el) return;
  el.textContent = new Date().toLocaleDateString('hi-IN', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
  });
}

function setupMobileMenu() {
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('nav-menu');
  if (btn && menu) btn.onclick = () => menu.classList.toggle('active');
}

// ================= CATEGORIES =================
async function loadCategories() {
  const navMenu = document.getElementById('nav-menu');
  const categories = await fetchData('/categories/');

  if (!navMenu) return;
  navMenu.innerHTML = '';

  categories.forEach(cat => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="category.html?category=${cat.slug}">${cat.name}</a>`;
    navMenu.appendChild(li);
  });
}

// ================= HOME PAGE =================
async function loadTopHeadlines() {
  const box = document.getElementById('top-headlines');
  if (!box) return;

  const news = await fetchData('/news/?limit=6');
  box.innerHTML = '';

  news.forEach(n => {
    box.innerHTML += `
      <div class="headline-card">
        <a href="news-detail.html?id=${n.id}">
          <img src="${n.image || ''}">
          <h3>${n.title}</h3>
        </a>
      </div>`;
  });
}

async function setupCategoryTabs() {
  const tabs = document.getElementById('category-tabs');
  const content = document.getElementById('category-news-content');
  if (!tabs || !content) return;

  const categories = await fetchData('/categories/');
  tabs.innerHTML = '';

  categories.forEach((cat, i) => {
    const a = document.createElement('a');
    a.textContent = cat.name;
    a.href = '#';
    a.dataset.slug = cat.slug;
    if (i === 0) {
      a.classList.add('active');
      currentCategory = cat.slug;
    }
    a.onclick = e => {
      e.preventDefault();
      document.querySelector('.category-tab.active')?.classList.remove('active');
      a.classList.add('active');
      currentCategory = cat.slug;
      loadCategoryNews(cat.slug, content);
    };
    a.className = 'category-tab';
    tabs.appendChild(a);
  });

  loadCategoryNews(currentCategory, content);
}

async function loadCategoryNews(slug, container) {
  const news = await fetchData(`/news/?category=${slug}&limit=5`);
  container.innerHTML = '';

  news.forEach(n => {
    container.innerHTML += `
      <div class="news-list-item">
        <a href="news-detail.html?id=${n.id}">
          <img src="${n.image || ''}">
          <h4>${n.title}</h4>
        </a>
      </div>`;
  });
}

// ================= CATEGORY PAGE =================
async function loadCategoryPage() {
  const params = new URLSearchParams(window.location.search);
  const slug = params.get('category');

  const title = document.getElementById('category-title');
  const list = document.getElementById('category-news-list');

  const categories = await fetchData('/categories/');
  const current = categories.find(c => c.slug === slug);

  if (title && current) title.textContent = current.name;
  if (list) loadCategoryNews(slug, list);
}

// ================= NEWS DETAIL =================
async function loadNewsDetail() {
  const id = new URLSearchParams(window.location.search).get('id');
  if (!id) return location.href = 'index.html';

  const n = await fetchData(`/news/${id}/`);
  document.getElementById('news-title').textContent = n.title;
  document.getElementById('news-content').innerHTML = n.description;
  document.getElementById('news-category').textContent = n.category_name;
}

async function loadRelatedNews() {
  const id = new URLSearchParams(window.location.search).get('id');
  const current = await fetchData(`/news/${id}/`);
  const related = await fetchData(`/news/?category=${current.category_slug}&limit=4`);

  const box = document.getElementById('related-news');
  box.innerHTML = '';
  related.filter(n => n.id != id).forEach(n => {
    box.innerHTML += `<a href="news-detail.html?id=${n.id}">${n.title}</a>`;
  });
}

// ================= SIDEBAR =================
async function loadLatestNews() {
  const box = document.getElementById('latest-news');
  if (!box) return;

  const news = await fetchData('/news/?limit=5');
  box.innerHTML = '';
  news.forEach(n => box.innerHTML += `<a href="news-detail.html?id=${n.id}">${n.title}</a>`);
}

async function loadEpaper() {
  const box = document.getElementById('epaper-box');
  if (!box) return;

  const e = await fetchData('/epaper/latest/');
  if (!e) return;

  box.innerHTML = `<a href="${e.pdf_file}" target="_blank">आज का ई-पेपर</a>`;
}
