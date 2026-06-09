import { http } from './http'

export const memberApi = {
  list: (keyword, levelId) => {
    const params = {}
    if (keyword) params.keyword = keyword
    if (levelId) params.level_id = levelId
    return http.get('/members', { params })
  },
  create: (payload) => http.post('/members', payload),
  update: (id, payload) => http.patch(`/members/${id}`, payload),
}
