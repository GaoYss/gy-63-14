import { http } from './http'

export const memberApi = {
  list: (keyword) => {
    const params = {}
    if (keyword) params.keyword = keyword
    return http.get('/members', { params })
  },
  create: (payload) => http.post('/members', payload),
  update: (id, payload) => http.patch(`/members/${id}`, payload),
}
