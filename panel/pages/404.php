<?php
// Xtream Codes Modern - 404 Page
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | Xtream Codes Modern</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0a0a0a; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 100vh; }
        .container { text-align: center; max-width: 600px; padding: 40px; }
        .error-code { font-size: 120px; font-weight: 900; background: linear-gradient(135deg, #ff0000, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; }
        h1 { font-size: 28px; margin: 20px 0 10px; }
        p { color: #888; margin-bottom: 30px; line-height: 1.6; }
        .btn { display: inline-block; padding: 12px 32px; background: #ff0000; color: #fff; text-decoration: none; border-radius: 8px; font-weight: 600; transition: transform 0.2s; }
        .btn:hover { transform: translateY(-2px); background: #e60000; }
        .icon { font-size: 48px; margin-bottom: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">📡</div>
        <div class="error-code">404</div>
        <h1>Page Not Found</h1>
        <p>The page you're looking for doesn't exist or has been moved.<br>Let's get you back on track.</p>
        <a href="/" class="btn">Back to Dashboard</a>
    </div>
</body>
</html>