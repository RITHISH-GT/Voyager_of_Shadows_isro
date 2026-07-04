import numpy as np
import heapq

W_BASE           = 1.0
W_ROUGH_PENALTY  = 4.0
W_SHADOW_DRAIN   = 3.0
SHADOW_RUN_PENALTY = 0.25
MAX_SHADOW_RUN   = 40

def build_cost_map(rough_mask, shadow_mask, lit_mask,
                   boulder_mask, edge_mask):
    cost = np.full(rough_mask.shape, W_BASE, float)
    cost[rough_mask]  *= W_ROUGH_PENALTY
    cost[shadow_mask] *= W_SHADOW_DRAIN
    cost[edge_mask]    = np.inf
    cost[boulder_mask] = np.inf
    return cost

def astar_solar(cost, shadow, start, goal):
    H, W = cost.shape
    def h(a):
        return ((a[0]-goal[0])**2+(a[1]-goal[1])**2)**0.5
    nbrs = [(-1,0,1),(1,0,1),(0,-1,1),(0,1,1),
            (-1,-1,2**.5),(-1,1,2**.5),
            (1,-1,2**.5),(1,1,2**.5)]
    s = (start, 0)
    openq  = [(h(start), 0.0, s)]
    gscore = {s: 0.0}
    came   = {}
    while openq:
        _, gc, (cur, run) = heapq.heappop(openq)
        if cur == goal:
            path = [cur]; st = (cur, run)
            while st in came:
                st = came[st]; path.append(st[0])
            return path[::-1]
        if gc > gscore.get((cur,run), 1e18):
            continue
        for dr, dc, mv in nbrs:
            nr, nc = cur[0]+dr, cur[1]+dc
            if not (0<=nr<H and 0<=nc<W):
                continue
            c = cost[nr, nc]
            if not np.isfinite(c):
                continue
            in_sh = shadow[nr, nc]
            nrun  = run+1 if in_sh else 0
            if nrun > MAX_SHADOW_RUN:
                continue
            extra = SHADOW_RUN_PENALTY*run if in_sh else 0.0
            ng    = gc + mv*c + extra
            ns    = ((nr,nc), nrun)
            if ng < gscore.get(ns, 1e18):
                gscore[ns] = ng
                came[ns]   = (cur, run)
                heapq.heappush(
                    openq,(ng+h((nr,nc)),ng,ns))
    return None