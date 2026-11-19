<?php
// Xtream Codes Modern - Settings Page
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Settings | Xtream Codes Modern</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0a0a0a; color: #fff; }
        
        .sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 260px; background: #111; border-right: 1px solid #222; padding: 24px 16px; }
        .logo { font-size: 22px; font-weight: 700; margin-bottom: 32px; padding: 0 12px; }
        .nav-item { display: flex; align-items: center; padding: 12px 16px; margin: 4px 0; border-radius: 8px; color: #888; text-decoration: none; transition: all 0.2s; }
        .nav-item:hover, .nav-item.active { background: #1a1a1a; color: #fff; }
        .nav-item.active { border-left: 3px solid #ff0000; }
        
        .main { margin-left: 260px; padding: 32px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
        .header h1 { font-size: 28px; }
        
        .panel { background: #111; border: 1px solid #222; border-radius: 12px; overflow: hidden; }
        .panel-header { padding: 20px 24px; border-bottom: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }
        
        .form-group { padding: 20px 24px; border-bottom: 1px solid #222; }
        .form-group:last-child { border-bottom: none; }
        .form-label { display: block; margin-bottom: 8px; color: #888; font-size: 14px; }
        .form-input { width: 100%; padding: 12px 16px; background: #1a1a1a; border: 1px solid #333; border-radius: 8px; color: #fff; font-size: 14px; }
        .form-input:focus { border-color: #ff0000; outline: none; }
        
        .btn { padding: 8px 20px; border-radius: 8px; border: none; cursor: pointer; font-size: 14px; font-weight: 600; transition: all 0.2s; }
        .btn-primary { background: #ff0000; color: #fff; }
        .btn-primary:hover { background: #e60000; }
    </style>
</head>
<body>
    <aside class="sidebar">
        <div class="logo">X<span>tream</span> Codes</div>
        <nav>
            <a href="/?page=dashboard" class="nav-item">📊 Dashboard</a>
            <a href="/?page=streams" class="nav-item">📺 Live Streams</a>
            <a href="/?page=vod" class="nav-item">🎬 VOD Library</a>
            <a href="/?page=users" class="nav-item">👥 Users</a>
            <a href="/?page=subscriptions" class="nav-item">💳 Subscriptions</a>
            <a href="/?page=settings" class="nav-item active">⚙️ Settings</a>
            <a href="/?page=logout" class="nav-item">🚪 Logout</a>
        </nav>
    </aside>
    
    <main class="main">
        <div class="header"><div><h1>Settings</h1></div></div>
        
        <div class="panel">
            <div class="panel-header"><h2>System Configuration</h2></div>
            
            <div class="form-group">
                <label class="form-label">Application Name</label>
                <input class="form-input" type="text" value="Xtream Codes Modern">
            </div>
            
            <div class="form-group">
                <label class="form-label">Database Host</label>
                <input class="form-input" type="text" value="database">
            </div>
            
            <div class="form-group">
                <label class="form-label">RTMP Stream Port</label>
                <input class="form-input" type="number" value="1935">
            </div>
            
            <div class="form-group">
                <label class="form-label">HLS Output Directory</label>
                <input class="form-input" type="text" value="/var/www/html/hls">
            </div>
            
            <div class="form-group" style="text-align:right;">
                <button class="btn btn-primary">Save Changes</button>
            </div>
        </div>
    </main>
</body>
</html>