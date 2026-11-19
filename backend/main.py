#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Xtream Codes Modern - FastAPI Backend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, streams, subscriptions, notifications, auth

app = FastAPI(
    title="Xtream Codes Modern API",
    description="API for managing Xtream Codes IPTV system",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(streams.router)
app.include_router(subscriptions.router)
app.include_router(notifications.router)

@app.get("/")
async def root():
    return {"message": "Xtream Codes Modern API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}