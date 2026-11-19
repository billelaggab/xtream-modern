<?php
// Xtream Codes Modern - Dashboard Page
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Xtream Codes Modern</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0a0a0a; color: #fff; }
        
        /* Sidebar */
        .sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 260px; background: #111; border-right: 1px solid #222; padding: 24px 16px; }
        .logo { font-size: 22px; font-weight: 700; margin-bottom: 32px; padding: 0 12px; }
        .logo span { color: #ff0000; }
        .nav-item { display: flex; align-items: center; padding: 12px 16px; margin: 4px 0; border-radius: 8px; color: #888; text-decoration: none; transition: all 0.2s; }
        .nav-item:hover, .nav-item.active { background: #1a1a1a; color: #fff; }
        .nav-item.active { border-left: 3px solid #ff0000; }
        
        /* Main Content */
        .main { margin-left: 260px; padding: 32px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
        .header h1 { font-size: 28px; }
        .user-menu { display: flex; align-items: center; gap: 16px; }
        .user-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #ff0000, #ff6b6b); display: flex; align-items: center; justify-content: center; font-weight: 700; }
        
        /* Stats Grid */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px; margin-bottom: 32px; }
        .stat-card { background: #111; border: 1px solid #222; border-radius: 12px; padding: 24px; transition: transform 0.2s, border-color 0.2s; }
        .stat-card:hover { transform: translateY(-4px); border-color: #ff0000; }
        .stat-icon { font-size: 32px; margin-bottom: 16px; }
        .stat-label { color: #888; font-size: 14px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }
        .stat-value { font-size: 32px; font-weight: 700; }
        .stat-change { font-size: 14px; margin-top: 8px; }
        .stat-change.up { color: #00ff88; }
        .stat-change.down { color: #ff4444; }
        
        /* Table */
        .panel { background: #111; border: 1px solid #222; border-radius: 12px; overflow: hidden; }
        .panel-header { padding: 20px 24px; border-bottom: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }
        .panel-header h2 { font-size: 18px; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 16px 24px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #888; border-bottom: 1px solid #222; }
        td { padding: 16px 24px; border-bottom: 1px solid #222; }
        tr:last-child td { border-bottom: none; }
        tr:hover td { background: #1a1a1a; }
        
        /* Badges */
        .badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-live { background: rgba(0,255,136,0.1); color: #00ff88; }
        .badge-offline { background: rgba(255,68,68,0.1); color: #ff4444; }
        .badge-vod { background: rgba(0,150,255,0.1); color: #0096ff; }
        .badge-subscriber { background: rgba(255,200,0,0.1); color: #ffc800; }
        
        /* Buttons */
        .btn { padding: 8px 20px; border-radius: 8px; border: none; cursor: pointer; font-size: 14px; font-weight: 600; transition: all 0.2s; }
        .btn-primary { background: #ff0000; color: #fff; }
        .btn-primary:hover { background: #e60000; }
        .btn-ghost { background: transparent; color: #fff; border: 1px solid #333; }
        .btn-ghost:hover { border-color: #ff0000; }
    </style>
</head>
<body>
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="logo">X<span>tream</span> Codes</div>
        <nav>
            <a href="/" class="nav-item active">📊 Dashboard</a>
            <a href="/?page=streams" class="nav-item">📺 Live Streams</a>
            <a href="/?page=vod" class="nav-item">🎬 VOD Library</a>
            <a href="/?page=users" class="nav-item">👥 Users</a>
            <a href="/?page=subscriptions" class="nav-item">💳 Subscriptions</a>
            <a href="/?page=settings" class="nav-item">⚙️ Settings</a>
            <a href="/?page=logout" class="nav-item">🚪 Logout</a>
        </nav>
    </aside>
    
    <!-- Main Content -->
    <main class="main">
        <div class="header">
            <div>
                <h1>Dashboard</h1>
                <p style="color:#888; margin-top:8px;">Welcome back, Administrator</p>
            </div>
            <div class="user-menu">
                <span style="color:#888;">Admin</span>
                <div class="user-avatar">A</div>
            </div>
        </div>
        
        <!-- Stats -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon">📺</div>
                <div class="stat-label">Live Streams</div>
                <div class="stat-value">124</div>
                <div class="stat-change up">↑ 12% from last week</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">👥</div>
                <div class="stat-label">Active Subscribers</div>
                <div class="stat-value">2,847</div>
                <div class="stat-change up">↑ 8% from last week</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🎬</div>
                <div class="stat-label">VOD Items</div>
                <div class="stat-value">1,532</div>
                <div class="stat-change up">↑ 24% from last week</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">📡</div>
                <div class="stat-label">Bandwidth Today</div>
                <div class="stat-value">2.4 TB</div>
                <div class="stat-change up">↑ 15% from yesterday</div>
            </div>
        </div>
        
        <!-- Recent Streams -->
        <div class="panel">
            <div class="panel-header">
                <h2>Recent Live Streams</h2>
                <a href="/?page=streams" class="btn btn-ghost">View All</a>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Channel</th>
                        <th>Status</th>
                        <th>Viewers</th>
                        <th>Bitrate</th>
                        <th>Started</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Sports HD</strong></td>
                        <td><span class="badge badge-live">● Live</span></td>
                        <td>1,245</td>
                        <td>2.5 Mbps</td>
                        <td>2 hours ago</td>
                        <td><button class="btn btn-ghost" style="padding:4px 12px;">⋮</button></td>
                    </tr>
                    <tr>
                        <td><strong>News 24/7</strong></td>
                        <td><span class="badge badge-live">● Live</span></td>
                        <td>856</td>
                        <td>1.8 Mbps</td>
                        <td>4 hours ago</td>
                        <td><button class="btn btn-ghost" style="padding:4px 12px;">⋮</button></td>
                    </tr>
                    <tr>
                        <td><strong>Movies Premium</strong></td>
                        <td><span class="badge badge-vod">VOD</span></td>
                        <td>-</td>
                        <td>-</td>
                        <td>24 items</td>
                        <td><button class="btn btn-ghost" style="padding:4px 12px;">⋮</button></td>
                    </tr>
                    <tr>
                        <td><strong>Kids Zone</strong></td>
                        <td><span class="badge badge-offline">Offline</span></td>
                        <td>0</td>
                        <td>-</td>
                        <td>Stopped 1 hour ago</td>
                        <td><button class="btn btn-ghost" style="padding:4px 12px;">⋮</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>