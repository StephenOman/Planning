import gym
import minihack
import state
import glyphs
import action
import planner
import numpy as np
import logging
import datetime


# Set up some logging
output_dir = 'output'
log_format = '%(asctime)-15s %(name)s %(message)s'
now = datetime.datetime.now()
log_file = output_dir + '/find_stair_1' + now.strftime("%Y%m%d%H%M%S") + '.log'
logging.basicConfig(format=log_format, filename=log_file, level=logging.DEBUG)
logger = logging.getLogger(__name__)

# start up the gym

env = gym.make('MiniHack-Room-Random-15x15-v0', savedir = output_dir)
obs = env.reset()

env.render()

stair_loc = None

# Find where the stairs are and make that the goal state
for row in range(0,obs['glyphs'].shape[0]):
    try:
        col = np.where(obs['glyphs'][row] == glyphs.STAIR_DOWN)[0][0]
        stair_loc = (row, col)
    except IndexError:
        pass

if stair_loc:
    agent_start = state.State((obs['blstats'][1], obs['blstats'][0]))
    goal = state.State(stair_loc)

    actions = [action.Action('N', (-1, 0), 0), action.Action('S', (1, 0), 2), 
               action.Action('E', (0, 1), 1), action.Action('W', (0, -1), 3),
               action.Action('NE', (-1, 1), 4), action.Action('SE', (1, 1), 5), 
               action.Action('NW', (-1, -1), 7), action.Action('SW', (1, -1), 6)]

    logger.debug("Agent Location: " + str(agent_start.location))
    logger.debug("Goal location: " + str(goal.location))
    #planner_basic = planner.Breadth_First_Planner(agent_start, goal, actions)
    planner_basic = planner.Depth_First_Planner(agent_start, goal, actions)
    if planner_basic.plan(obs['glyphs']):
        for act in planner_basic.goal_node.plan:
            obs, reward, done, info = env.step(act.step)
            env.render()

        logger.debug("Plan execution complete")
        logger.debug("Reward: " + str(reward))
    else:
        logger.debug("No route found")

else:
    logger.debug("Can't find the stairs")



