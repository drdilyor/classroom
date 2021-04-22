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
            return part
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
