import { defineMermaidSetup } from '@slidev/types'

// Mermaid can't read CSS variables; these mirror external/sdsc-slides/references/tokens.toml.
export default defineMermaidSetup(() => ({
  theme: 'base',
  themeVariables: {
    fontFamily: 'Switzer, Calibri, sans-serif',
    primaryColor: '#DDDEEC',
    primaryTextColor: '#26235C',
    primaryBorderColor: '#5561A6',
    secondaryColor: '#F4F3F8',
    tertiaryColor: '#FFFFFF',
    lineColor: '#5561A6',
    edgeLabelBackground: '#FFFFFF',
  },
}))
