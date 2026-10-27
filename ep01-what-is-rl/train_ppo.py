"""Trains the PPO agent used in episodes 1 and 2 (LunarLander-v3, 1,000,000 steps).

About 20-40 minutes on a CPU. The trained model is saved next to this file as ppo-LunarLander-v3.zip.
"""
from pathlib import Path

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

HERE = Path(__file__).resolve().parent

env = make_vec_env("LunarLander-v3", n_envs=16, seed=0)
model = PPO("MlpPolicy", env, n_steps=1024, batch_size=64, n_epochs=4,
            gamma=0.999, gae_lambda=0.98, ent_coef=0.01, seed=0, verbose=1)
model.learn(total_timesteps=1_000_000)
model.save(HERE / "ppo-LunarLander-v3")
print("saved", HERE / "ppo-LunarLander-v3.zip")
