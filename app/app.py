from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Projet DevOps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.6;
        }
        .container { max-width: 900px; margin: 0 auto; padding: 60px 20px; }
        header { text-align: center; margin-bottom: 60px; }
        h1 {
            font-size: 2.5rem;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .subtitle { color: #94a3b8; margin-top: 10px; font-size: 1.1rem; }
        .badge-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-top: 20px; }
        .badge {
            background: #1e293b;
            border: 1px solid #334155;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            color: #38bdf8;
        }
        .pipeline {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin: 40px 0;
        }
        .step {
            background: #1e293b;
            border-left: 4px solid #38bdf8;
            padding: 20px 24px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .step-num {
            background: #38bdf8;
            color: #0f172a;
            font-weight: bold;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .step-content h3 { font-size: 1.05rem; margin-bottom: 4px; }
        .step-content p { color: #94a3b8; font-size: 0.9rem; }
        .status {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            background: #1e293b;
            border-radius: 8px;
        }
        .status .dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #4ade80;
            border-radius: 50%;
            margin-right: 8px;
        }
        footer { text-align: center; margin-top: 50px; color: #64748b; font-size: 0.85rem; }
        a { color: #38bdf8; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Mon Projet DevOps</h1>
            <p class="subtitle">De zéro à la production, en toute autonomie</p>
            <div class="badge-row">
                <span class="badge">Flask</span>
                <span class="badge">Docker</span>
                <span class="badge">GitHub Actions</span>
                <span class="badge">Oracle Cloud</span>
                <span class="badge">Nginx</span>
                <span class="badge">Let's Encrypt</span>
            </div>
        </header>

        <div class="pipeline">
            <div class="step">
                <div class="step-num">1</div>
                <div class="step-content">
                    <h3>Code &amp; Versioning</h3>
                    <p>Application Flask versionnée sur GitHub</p>
                </div>
            </div>
            <div class="step">
                <div class="step-num">2</div>
                <div class="step-content">
                    <h3>Conteneurisation</h3>
                    <p>Image Docker construite à partir d'un Dockerfile</p>
                </div>
            </div>
            <div class="step">
                <div class="step-num">3</div>
                <div class="step-content">
                    <h3>Intégration Continue</h3>
                    <p>GitHub Actions build et teste automatiquement à chaque push</p>
                </div>
            </div>
            <div class="step">
                <div class="step-num">4</div>
                <div class="step-content">
                    <h3>Déploiement Continu</h3>
                    <p>Déploiement automatique sur une VM Oracle Cloud via SSH</p>
                </div>
            </div>
            <div class="step">
                <div class="step-num">5</div>
                <div class="step-content">
                    <h3>Nginx &amp; HTTPS</h3>
                    <p>Reverse proxy Nginx avec certificat SSL Let's Encrypt</p>
                </div>
            </div>
        </div>

        <div class="status">
            <span class="dot"></span> Application en ligne — <a href="/health">/health</a>
        </div>

        <footer>
            Construit étape par étape, avec ses erreurs et ses réussites.
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
