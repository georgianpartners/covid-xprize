import gym
import gym_covid


env = gym.make("covid-env-v0")
observation = env.reset()

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()