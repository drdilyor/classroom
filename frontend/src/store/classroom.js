import api from "../api"

export default {
  state: {
    currentCourse: null,
    currentLessonId: null,
  },
  
  mutations: {
    setCourse(state, course) {
      state.currentCourse = course
    },
    setLessonId(state, lessonId) {
      state.currentLessonId = lessonId
    },
    lessonViewed(_state, lesson) {
      lesson.is_viewed = true
    }
  },
  
  actions: {
    async setCourse({ commit, getters }, courseId) {
      if (getters.currentCourse?.id == courseId)
        return
      console.log('setCourse cache miss '+courseId);
      commit('setCourse', null)
      api.get('/enrolled-courses/'+courseId)
      .then(course => commit('setCourse', course))
    },
    
    async setLesson({ commit, getters, dispatch }, lessonId) {
      commit('setLessonId', lessonId)
      console.log('setLesson '+lessonId)
      if (typeof(getters.getLesson(lessonId)) === 'object')
        return
      dispatch('setCourse', (await api.get('/lessons/'+lessonId)).course_id)
    },
    
    async lessonViewed({ commit, getters }, lessonId) {
      api.request('PUT', `/lessons/${lessonId}/viewed`)
      .then(() => {
        const lesson = getters.getLesson(lessonId)
        if (lesson) commit('lessonViewed', lesson)
      })
    }
  },

  getters: {
    currentCourse(state) {
      return state.currentCourse
    },
    currentPart(state) {
      if (state.currentLessonId === null || state.currentCourse === null)
        return null

      let result = null
      for (const part of state.currentCourse.course_parts) {
        for (const lesson of part.lessons) {
          if (lesson.id === state.currentLessonId) {
            result = part
            break
          }
        }
      }
      
      console.log({currentPart: result})
      return result
    },
    currentLesson(state, { getLesson }) {
      return getLesson(state.currentLessonId)
    },
    getLesson: (state) => (id) => {
      if (state.currentCourse === null)
        return
      let result = null
      outer:
      for (const part of state.currentCourse.course_parts)
        for (const lesson of part.lessons)
          if (lesson.id == id) {
            result = lesson
            break outer
          }
      console.log({result});
      return result
    }
  }
}
