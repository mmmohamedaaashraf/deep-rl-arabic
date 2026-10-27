"""Trains a PPO agent on LunarLander-v3 for 1,000,000 steps, with the settings of the model used in episodes 1 and 2.

About 20-40 minutes on a CPU. A new run gives a model of similar quality, not the exact same weights, so it is
saved under its own name and the episode model (ppo-LunarLander-v3.zip) is kept.
"""
from pathlib import Path

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

HERE = Path(__file__).resolve().parent

env = make_vec_env("LunarLander-v3", n_envs=16, seed=0)
model = PPO("MlpPolicy", env, n_steps=1024, batch_size=64, n_epochs=4,
            gamma=0.999, gae_lambda=0.98, ent_coef=0.01, seed=0, verbose=1)
model.learn(total_timesteps=1_000_000)
model.save(HERE / "my-ppo-LunarLander-v3")
print("saved", HERE / "my-ppo-LunarLander-v3.zip")
