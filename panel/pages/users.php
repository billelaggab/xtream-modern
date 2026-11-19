<?php
// Xtream Codes Modern - Users Page
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users | Xtream Codes Modern</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0a0a0a; color: #fff; }
        
        .sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 260px; background: #111; border-right: 1px solid #222; padding: 24px 16px; }
        .logo { font-size: 22px; font-weight: 700; margin-bottom: 32px; padding: 0 12px; }
        .logo span { color: #ff0000; }
        .nav-item { display: flex; align-items: center; padding: 12px 16px; margin: 4px 0; border-radius: 8px; color: #888; text-decoration: none; transition: all 0.2s; }
        .nav-item:hover, .nav-item.active { background: #1a1a1a; color: #fff; }
        .nav-item.active { border-left: 3px solid #ff0000; }
        
        .main { margin-left: 260px; padding: 32px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
        .header h1 { font-size: 28px; }
        
        .panel { background: #111; border: 1px solid #222; border-radius: 12px; overflow: hidden; }
        .panel-header { padding: 20px 24px; border-bottom: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }
        
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 16px 24px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #888; border-bottom: 1px solid #222; }
        td { padding: 16px 24px; border-bottom: 1px solid #222; }
        tr:last-child td { border-bottom: none; }
        tr:hover td { background: #1a1a1a; }
        
        .badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-admin { background: rgba(255,0,0,0.1); color: #ff0000; }
        .badge-user { background: rgba(0,150,255,0.1); color: #0096ff; }
        .badge-viewer { background: rgba(100,100,100,0.1); color: #888; }
        .badge-active { background: rgba(0,255,136,0.1); color: #00ff88; }
        .badge-inactive { background: rgba(255,68,68,0.1); color: #ff4444; }
        
        .btn { padding: 8px 20px; border-radius: 8px; border: none; cursor: pointer; font-size: 14px; font-weight: 600; transition: all 0.2s; }
        .btn-primary { background: #ff0000; color: #fff; }
        .btn-ghost { background: transparent; color: #fff; border: 1px solid #333; }
        .actions { display: flex; gap: 8px; }
    </style>
</head>
<body>
    <aside class="sidebar">
        <div class="logo">X<span>tream</span> Codes</div>
        <nav>
            <a href="/?page=dashboard" class="nav-item">📊 Dashboard</a>
            <a href="/?page=streams" class="nav-item">📺 Live Streams</a>
            <a href="/?page=vod" class="nav-item">🎬 VOD Library</a>
            <a href="/?page=users" class="nav-item active">👥 Users</a>
            <a href="/?page=subscriptions" class="nav-item">💳 Subscriptions</a>
            <a href="/?page=settings" class="nav-item">⚙️ Settings</a>
            <a href="/?page=logout" class="nav-item">🚪 Logout</a>
        </nav>
    </aside>
    
    <main class="main">
        <div class="header">
            <div>
                <h1>Users</h1>
                <p style="color:#888; margin-top:8px;">Manage system users and permissions</p>
            </div>
            <button class="btn btn-primary">+ Add User</button>
        </div>
        
        <div class="panel">
            <div class="panel-header">
                <h2>All Users</h2>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Status</th>
                        <th>Created</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>admin</strong></td>
                        <td>admin@xtream.local</td>
                        <td><span class="badge badge-admin">Admin</span></td>
                        <td><span class="badge badge-active">Active</span></td>
                        <td>2024-01-15</td>
                        <td>
                            <div class="actions">
                                <button class="btn btn-ghost" style="padding:4px 12px;">Edit</button>
                                <button class="btn btn-ghost" style="padding:4px 12px; color:#ff4444; border-color:#ff4444;">Delete</button>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td><strong>john_doe</strong></td>
                        <td>john@example.com</td>
                        <td><span class="badge badge-user">User</span></td>
                        <td><span class="badge badge-active">Active</span></td>
                        <td>2024-02-20</td>
                        <td>
                            <div class="actions">
                                <button class="btn btn-ghost" style="padding:4px 12px;">Edit</button>
                                <button class="btn btn-ghost" style="padding:4px 12px; color:#ff4444; border-color:#ff4444;">Delete</button>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td><strong>viewer1</strong></td>
                        <td>viewer@example.com</td>
                        <td><span class="badge badge-viewer">Viewer</span></td>
                        <td><span class="badge badge-inactive">Inactive</span></td>
                        <td>2024-03-10</td>
                        <td>
                            <div class="actions">
                                <button class="btn btn-ghost" style="padding:4px 12px;">Edit</button>
                                <button class="btn btn-ghost" style="padding:4px 12px; color:#ff4444; border-color:#ff4444;">Delete</button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>