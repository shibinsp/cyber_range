import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface UIState {
  sidebarOpen: boolean
  commandPaletteOpen: boolean
  theme: 'retro' | 'dark' | 'light'
}

const initialState: UIState = {
  sidebarOpen: true,
  commandPaletteOpen: false,
  theme: 'retro',
}

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleSidebar: (state) => {
      state.sidebarOpen = !state.sidebarOpen
    },
    toggleCommandPalette: (state) => {
      state.commandPaletteOpen = !state.commandPaletteOpen
    },
    setTheme: (state, action: PayloadAction<'retro' | 'dark' | 'light'>) => {
      state.theme = action.payload
    },
  },
})

export const { toggleSidebar, toggleCommandPalette, setTheme } = uiSlice.actions
export default uiSlice.reducer
