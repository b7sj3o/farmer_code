
<h1>Farmer Code</h1>
<p><strong>Farmer Code</strong> - це гра, що є адаптацією "The farmer was replaced". Вона знаходиться на етапі розробки і має багато помилок, оскільки не була повністю рефакторизована.</p>

<h2>Налаштування Проекту</h2>
<p>Щоб розпочати роботу з проектом, виконайте наступні кроки:</p>
<ol>
    <li>Клонуйте репозиторій:
        <pre><code>git clone https://github.com/b7sj3o/farmer_code.git</code></pre>
    </li>
    <li>Перейдіть до директорії проекту:
        <pre><code>cd farmer_code</code></pre>
    </li>
    <li>Створіть і активуйте віртуальне середовище:
        <pre><code>python -m venv .venv
# Для Windows
.venv\Scripts\activate
# Для MacOS/Linux
source .venv/bin/activate</code></pre>
        </li>
        <li>Встановіть залежності:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Створіть файл .env згідно .env.example:
        </li>
        <li>Запустіть програму:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

<h2>Логін до Гри</h2>
<p>Щоб увійти в гру, виконайте наступні кроки:</p>
<ol>
    <li>Відкрийте Telegram і знайдіть бота <a href="https://t.me/farmercode_bot">@farmercode_bot</a>.</li>
    <li>Введіть свій юзернейм у чаті з ботом і підтвердіть логін.</li>
</ol>

<h2>Доступні Функції</h2>
<p>У грі доступні наступні функції:</p>
<ul>
    <li><code>harvest()</code>: Збирає урожай.</li>
    <li><code>move(direction)</code>: Рухається в зазначеному напрямку (<code>North</code>, <code>South</code>, <code>East</code>, <code>West</code>).</li>
    <li><code>get_pos_x()</code>: Повертає координату робота по осі X.</li>
    <li><code>get_pos_y()</code>: Повертає координату робота по осі Y.</li>
    <li><code>plant(plant_type)</code>: Посаджує рослину (наразі підтримується тільки <code>Wheat</code>).</li>
</ul>
